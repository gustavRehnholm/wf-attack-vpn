#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/generate_merged_dataset/main.py
'''

import random
import pandas as pd
import os
import timeit

def mergeTraffic(mergedFiles, foregroundFiles, background_path, start, stop):
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

    print("Start merging subset(can take some time to move the background to memory)")

    # access the foreground packets time
    PACKET_ATTR_INDEX_TIME = 0
    # to access the background data in the hdf5 file
    KEY = "df"
    # index to access the values for the background packages
    TIME_INDEX      = 0
    DIRECTION_INDEX = 1
    SIZE_INDEX      = 2 
    # all lines in the open foreground file
    foreground_lines = []
    # timestamp of the current background packets
    time_stamp = 0
    # the background traffic: use the tuple for performance
    df               = pd.read_hdf(path_or_buf = background_path, key = KEY, start = start, stop = stop)
    # list with indexes [0, background_nr_packets[
    background_tuple      = list(df.itertuples(index=False, name=None))
    background_nr_packets = len(background_tuple)
    df_len = df.shape[0]
    if background_nr_packets != df_len:
        print("tuple has not the same size as the df")
        return False
    # current index to get background from
    subset_index = 0
    # for testing
    added_foreground = True
    # seed the rnd generator
    random.seed(timeit.default_timer())

    totalMergeFiles = len(mergedFiles)
    mergeFilesDone = 0

    while(len(foregroundFiles) > 0): 

            # if should open a new foreground file
            if len(foreground_lines) <= 0:

                # for testing
                if added_foreground == False:
                    print("The foreground file ", os.path.basename(foregroundFiles[0]), " was not injected with any foreground")
                    return False

                added_foreground = False
                # reset the time stamp for the background packets
                prev_time = 0
                # get a new randomized stating position
                df_index = random.randrange(0, background_nr_packets)

                mergeFilesDone += 1
                printProgressBar(progress = mergeFilesDone, progressLen = totalMergeFiles, prefix = 'Progress:', suffix = 'Complete')

                # get the values (lines) of the new foreground file
                currForegroundFile = open(foregroundFiles[0], 'r') 
                foreground_lines   = currForegroundFile.readlines()
                currForegroundFile.close()
                foregroundFiles.pop(0)

                # open the merged file, that the result will be stored to
                currMergedFile = open(mergedFiles[0], 'a')
                mergedFiles.pop(0)

            foreground_time = int(foreground_lines[0].split(",")[PACKET_ATTR_INDEX_TIME])
            # timestamp the current background packet is on
            curr_time = prev_time + int(background_tuple[df_index][TIME_INDEX])

            # add the packet that arrives first
            if(curr_time < foreground_time):
                currMergedFile.writelines([str(curr_time), ",", 
                                           str(background_tuple[df_index][DIRECTION_INDEX]), ",", 
                                           str(background_tuple[df_index][SIZE_INDEX]), "\n"])
                added_foreground = True
                prev_time = curr_time
                df_index += 1
                # if end of the background list, loop it from the start
                if df_index >= background_nr_packets:
                    df_index = 0
            else:
                currMergedFile.writelines(foreground_lines[0])
                foreground_lines.pop(0)
        
    return True


def printProgressBar (progress, progressLen, prefix = '', suffix = '', barLen = 50, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    args:
        progress    - Required  : current progress                                (Int)
        progressLen - Required  : total iterations                                (Int)
        prefix      - Optional  : prefix string                                   (Str)
        suffix      - Optional  : suffix string                                   (Str)
        barLen      - Optional  : character length of bar                         (Int)
        fill        - Optional  : bar fill character                              (Str)
    """
    txt          = "{perc:.1f}"
    percent      = txt.format(100 * (progress / float(progressLen)))
    progPercent  = int(progress / progressLen)
    filledLength = int(barLen * progPercent)
    bar          = fill * filledLength + '-' * (barLen - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = "\r")

    # Print New Line on Complete
    if progress == progressLen: 
        print()

if __name__=="__main__":
    main()