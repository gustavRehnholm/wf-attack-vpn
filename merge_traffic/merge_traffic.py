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

def mergeTraffic(mergedFiles, foregroundFiles, background_path, start, stop, workers):
    '''
    This program merges the web traffic with noise, so it can be used to test WF attacks

    Args:
        mergedFiles      - Required  : list of paths to the merged files                (List[str])
        foregroundFiles  - Required  : list of paths to the foreground files            (List[str])
        background_path  - Required  : path to the background file                      (str)
        start            - Required  : The start index of the background traffic to use (int)
        stop             - Required  : The end index of the background traffic to use   (int)
    Returns:
        boolean if the program succeeded or not in creating the merge files
    '''

    # access the foreground packets time
    PACKET_ATTR_INDEX_TIME = 0
    # to access the background data in the hdf5 file
    KEY = "df"
    # timestamp of the current background packets
    time_stamp = 0

    # the background traffic: use the tuple for performance
    df = pd.read_hdf(path_or_buf = background_path, key = KEY, start = start, stop = stop)
    # list with indexes [0, background_nr_packets[
    global background_tuple
    global background_nr_packets

    background_tuple      = list(df.itertuples(index=False, name=None))
    background_nr_packets = len(background_tuple)


    # current index to get background from
    subset_index = 0
    # for testing
    added_foreground = True
    # seed the rnd generator
    random.seed(timeit.default_timer())

    totalMergeFiles = len(mergedFiles)
    mergeFilesDone = 0

    p = Pool(workers)

    input = []
    for j in range(len(mergedFiles)):
        input.append((mergedFiles[j], foregroundFiles[j]))

    results = p.starmap(inject, input)

    if False in results:
        print("ERROR: failed to inject")
        return False
    else:
        return True

def inject(mergedFile, foregroundFile):
    '''
    Inject all foreground packets, with background to the merged file
    Input:
        mergedFile: path to the file where the result will be stored (string)
        foregroundFile: Path to the file where the foreground file is stored (string)
    Output:
        Boolean if it succeeded or not in creating the merged file
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
    currForegroundFile = open(foregroundFile, 'r') 
    foreground_lines = getStartForeground(currForegroundFile.readlines())
    currForegroundFile.close()

    # open the merged file, that the result will be stored to
    currMergedFile = open(mergedFile, 'a')

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
    By removing packets until the first 10 packets happens during one second
    Args:
        foreground_pkts - Required : all foreground packets (List)
    Return:
        Foreground packets without the delayed start (List)
    '''
    NS_PER_SEC = 1000000000
    PACKET_ATTR_INDEX_TIME = 0

    while(len(foreground_pkts) > 0):
        foreground_time_0 = int(foreground_pkts[0].split(",")[PACKET_ATTR_INDEX_TIME])
        foreground_time_4 = int(foreground_pkts[19].split(",")[PACKET_ATTR_INDEX_TIME])
        if (foreground_time_4 - foreground_time_0) < NS_PER_SEC:
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