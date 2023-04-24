#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/generate_merged_dataset/main.py
'''

import random
import pandas as pd
import os
import timeit
from multiprocessing import Pool

# storing the background data as a global variable, so the same list is accessible for all workers (multiprocessing)
global background_tuple
global background_nr_packets

def mergeTraffic(merged_files, foreground_files, background_path, start_index, end_index, workers = 5):
    '''
    This program merges the foreground and background datasets, so it can be used to test WF attacks

    Args:
        merged_files     - Required : list of paths to the merged files                (List[str])
        foreground_files - Required : list of paths to the foreground files            (List[str])
        background_path  - Required : path to the background file                      (str)
        start_index      - Required : The start index of the background traffic to use (int)
        end_index        - Required : The end index of the background traffic to use   (int)
        workers          - Optional : number of workers, multiprocessing (default = 5) (int)
    Returns:
        boolean if the program succeeded or not in creating the merge files             (bool)
    '''

    # to access the background data in the hdf5 file
    KEY = "df"

    # the background traffic: use the tuple for performance
    df = pd.read_hdf(path_or_buf = background_path, key = KEY, start = start_index, stop = end_index)
    # list with indexes [0, background_nr_packets[
    global background_tuple
    global background_nr_packets
    background_tuple      = list(df.itertuples(index=False, name=None))
    background_nr_packets = len(background_tuple)

    # seed the rnd generator
    random.seed(timeit.default_timer())

    p = Pool(workers)

    input = []
    for j in range(len(merged_files)):
        input.append((merged_files[j], foreground_files[j]))

    results = p.starmap(inject, input)

    if False in results:
        print("ERROR: failed to inject")
        return False
    else:
        return True

def inject(merged_file, foreground_file):
    '''
    Inject all foreground packets, with background to the merged file

    Args:
        merged_file     - Required : path to the file where the result will be stored     (str)
        foreground_file - Required : Path to the file where the foreground file is stored (str)
    Returns:
        Boolean if it succeeded or not in creating the merged file                        (bool)
    '''

    global background_tuple
    global background_nr_packets

    # index to access the values for the background packages
    TIME_INDEX      = 0
    DIRECTION_INDEX = 1
    SIZE_INDEX      = 2 
    # index for the foreground
    PACKET_ATTR_INDEX_TIME = 0
    # all lines in the open foreground file
    foreground_lines = []
    # reset the time stamp for the background packets
    prev_time = 0

    # get randomized stating position
    df_index = random.randrange(0, background_nr_packets)

    # get the values (lines) of the new foreground file
    currForegroundFile = open(foreground_file, 'r') 
    foreground_lines = getStartForeground(currForegroundFile.readlines())
    currForegroundFile.close()

    # open the merged file, that the result will be stored to
    currMergedFile = open(merged_file, 'a')

    foreground_time = int(foreground_lines[0].split(",")[PACKET_ATTR_INDEX_TIME])
    # timestamp the current background packet is on
    curr_time = prev_time + int(background_tuple[df_index][TIME_INDEX])

    # inject until 5000 packets has been injected to the merged dataset (DF does not make use of more than the first 5000 packets)
    for i in range(0, 5000):
        # add the packet that arrives first
        if(curr_time < foreground_time):
            currMergedFile.writelines([str(curr_time), ",", 
                                    str(background_tuple[df_index][DIRECTION_INDEX]), ",", 
                                    str(background_tuple[df_index][SIZE_INDEX]), "\n"])
            prev_time = curr_time
            df_index += 1
            # if end of the background list, loop it from the start
            if df_index >= background_nr_packets:
                df_index = 0
            curr_time = prev_time + int(background_tuple[df_index][TIME_INDEX])
        else:
            currMergedFile.writelines(foreground_lines[0])
            foreground_lines.pop(0)
            # end program if end of foreground lines
            if len(foreground_lines) > 0:
                foreground_time = int(foreground_lines[0].split(",")[PACKET_ATTR_INDEX_TIME])
            else:
                return True
    
    return True


def getStartForeground(foreground_pkts):
    '''
    removes the start delay of the foreground file
    By removing packets until the first 5 packets happens during one second
    Args:
        foreground_pkts - Required : all foreground packets (List)
    Return:
        Foreground packets without the delayed start (List)
    '''
    '''
    # FOR TESTING
    return foreground_pkts
    '''
    NS_PER_SEC = 1000000000
    time_between_pkt_group = NS_PER_SEC/100
    pkt_group_size = 5
    PACKET_ATTR_INDEX_TIME = 0

    while(len(foreground_pkts) > 0):
        foreground_time_first = int(foreground_pkts[0].split(",")[PACKET_ATTR_INDEX_TIME])
        foreground_time_end   = int(foreground_pkts[pkt_group_size - 1].split(",")[PACKET_ATTR_INDEX_TIME])
        if (foreground_time_end - foreground_time_first) < time_between_pkt_group:
            return foreground_pkts
        else:
            foreground_pkts.pop(0)

    print("ERROR: have removed all packets from the foreground")
    sys.exit()
    return []
    

def printProgressBar (progress, progressLen, prefix = '', suffix = '', barLen = 50, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    Args:
        progress    - Required  : current progress          (Int)
        progressLen - Required  : total iterations          (Int)
        prefix      - Optional  : prefix string             (Str)
        suffix      - Optional  : suffix string             (Str)
        barLen      - Optional  : character length of bar   (Int)
        fill        - Optional  : bar fill character        (Str)
    """
    curr_progress = 100 * (progress / float(progressLen))
    percent       = ("{0:.1f}").format(curr_progress)

    filledLength = int(barLen * progress // progressLen)
    bar          = fill * filledLength + '-' * (barLen - filledLength)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = "\r")

    # Print New Line on Complete
    if progress == progressLen: 
        print()

if __name__=="__main__":
    main()