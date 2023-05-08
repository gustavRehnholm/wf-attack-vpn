#!/usr/bin/python3

'''
TODO: Support multiple intervals (needed for b_fold)
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
global background_len

def mergeTraffic(merged_files, foreground_files, background_path, intervals, file_len = 5000, workers = 5):
    '''
    This program merges the foreground and background datasets, so it can be used to test WF attacks

    Args:
        merged_files     - Required : list of paths to the merged files                (List[str])
        foreground_files - Required : list of paths to the foreground files            (List[str])
        background_path  - Required : path to the background file                      (str)
        intervals         - Required : interval(s) to use from the background           (List[(int, int)])
        file_len         - Optional : number of packets per merged file                (int)
        workers          - Optional : number of workers, multiprocessing (default = 5) (int)
    Returns:
        boolean if the program succeeded or not in creating the merge files            (bool)
    '''

    # to access the background data in the hdf5 file
    KEY = "df"

    # TODO: check that one gets a correct merged dataframe
    dfs = []
    for interval_pair in intervals:
        # the background traffic: use the tuple for performance
        df_tmp = pd.read_hdf(path_or_buf = background_path, key = KEY, start = interval_pair[0], stop = interval_pair[1])
        df_len = df_tmp.shape[0]
        print(f"Added interval with {df_len} packets")
        dfs.append(df_tmp)

    df = pd.concat(dfs, axis = 1) 
    #print(f"Final size of df: {df.shape[0]}")

    # list with indexes [0, background_len[
    global background_tuple
    global background_len
    background_tuple = list(df.itertuples(index=False, name=None))
    background_len   = len(background_tuple)

    print(f"final size of background: {background_len}")

    print("--------------")
    print(background_tuple[0])
    print("--------------")
    print(background_tuple[0][0])
    print("--------------")
    print(background_tuple[1])
    print("--------------")
    print(background_tuple[1][0])
    print("--------------")

    # seed the rnd generator
    random.seed(timeit.default_timer())

    p = Pool(workers)

    input = []
    for j in range(len(merged_files)):
        input.append((merged_files[j], foreground_files[j], file_len))

    results = p.starmap(inject, input)

    if False in results:
        print("ERROR: failed to inject")
        return False
    else:
        return True

def inject(merged_path, foreground_path, file_len = 5000):
    '''
    Inject all foreground packets, with background to the merged file

    Args:
        merged_path     - Required : path to the file where the result will be stored     (str)
        foreground_path - Required : Path to the file where the foreground file is stored (str)
        file_len        - Optional : number of packets per merged file                    (int)
    Returns:
        Boolean if it succeeded or not in creating the merged file                        (bool)
    '''

    global background_tuple
    global background_len

    # index to access the values for the background packages
    TIME_INDEX      = 0
    DIRECTION_INDEX = 1
    SIZE_INDEX      = 2 
    # index for the foreground
    PACKET_ATTR_INDEX_TIME = 0

    # all lines in the open foreground file
    foreground_lines = []
    # reset the time stamp for the background packets
    prev_b_time = 0

    # get randomized stating position
    df_index = random.randrange(0, background_len)

    # get packets of the foreground file
    foreground_file = open(foreground_path, 'r') 
    foreground_lines = get_start_foreground(foreground_file.readlines())
    foreground_file.close()

    # open the merged file, that the result will be stored to
    merged_file = open(merged_path, 'a')

    # timestamp for the foreground and background packet
    foreground_time = int(foreground_lines[0].split(",")[PACKET_ATTR_INDEX_TIME])

    try:
        curr_b_time     = int(background_tuple[df_index][TIME_INDEX])
    except:
        print("Cannot convert to a int:")
        print(f"df_index: {df_index}")
        print(f"TIME_INDEX: {TIME_INDEX}")
        print(f"background_tuple[df_index][TIME_INDEX]: {background_tuple[df_index][TIME_INDEX]}")

    # inject until 5000 packets has been injected to the merged dataset (DF does not make use of more than the first 5000 packets)
    for i in range(0, file_len):
        # add the packet that arrives first
        if(curr_b_time < foreground_time):
            merged_file.writelines([str(curr_b_time), ",", 
                                    str(background_tuple[df_index][DIRECTION_INDEX]), ",", 
                                    str(background_tuple[df_index][SIZE_INDEX]), "\n"])
            prev_b_time = curr_b_time
            df_index += 1
            # if end of the background list, loop it from the start
            if df_index >= background_len:
                df_index = 0
            curr_b_time = prev_b_time + int(background_tuple[df_index][TIME_INDEX])
        else:
            merged_file.writelines(foreground_lines[0])
            foreground_lines.pop(0)
            # end program if end of foreground lines
            if len(foreground_lines) > 0:
                foreground_time = int(foreground_lines[0].split(",")[PACKET_ATTR_INDEX_TIME])
            else:
                return True
    
    return True


def get_start_foreground(foreground_pkts):
    '''
    removes the start delay of the foreground file
    By removing packets until the first 10 packets happens during 1/10 second
    Args:
        foreground_pkts - Required : all foreground packets (List[str])
    Return:
        Foreground packets without the delayed start        (List[str])
    '''
    '''
    return foreground_pkts
    '''

    NS_PER_SEC             = 1000000000
    TIME_BETWEEN_PKT_GROUP = NS_PER_SEC/10
    PKT_GROUP_SIZE         = 10
    PACKET_ATTR_INDEX_TIME = 0

    while(len(foreground_pkts) > 0):
        foreground_time_first = int(foreground_pkts[0].split(",")[PACKET_ATTR_INDEX_TIME])
        foreground_time_end   = int(foreground_pkts[PKT_GROUP_SIZE - 1].split(",")[PACKET_ATTR_INDEX_TIME])
        if (foreground_time_end - foreground_time_first) < TIME_BETWEEN_PKT_GROUP:
            return foreground_pkts
        else:
            foreground_pkts.pop(0)

    print("ERROR: have removed all packets from the foreground")
    sys.exit()
    return []
    
    

def print_progress_bar (progress, progress_len, prefix = '', suffix = '', bar_len = 50, fill = '█'):
    """
    Print a progressbar

    Args:
        progress     - Required  : current progress          (int)
        progress_len - Required  : total iterations          (int)
        prefix       - Optional  : prefix string             (str)
        suffix       - Optional  : suffix string             (str)
        bar_len      - Optional  : character length of bar   (int)
        fill         - Optional  : bar fill character        (str)
    """
    curr_progress = 100 * (progress / float(progress_len))
    percent       = ("{0:.1f}").format(curr_progress)

    filled_length = int(bar_len * progress // progress_len)
    bar           = fill * filled_length + '-' * (bar_len - filled_length)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = "\r")

    # Print New Line on Complete
    if progress == progress_len: 
        print()

if __name__=="__main__":
    main()