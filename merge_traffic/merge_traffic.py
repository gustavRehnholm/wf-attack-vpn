#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/generate_merged_dataset/main.py
'''

import random
import pandas as pd
import os
import timeit

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

input:
    mergedFiles:     list of paths to the merged files
    foregroundFiles: list of paths to the foreground files
    background_path: list of paths to the background files
    start:           The start index of the background traffic to use
    stop:            The end index of the background traffic to use
output:
    True:   it succeeded in creating the whole merged files
    False: it did not succeed
'''
def mergeTraffic(mergedFiles, foregroundFiles, background_path, start, stop):

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
    # the background traffic
    df     = pd.read_hdf(path_or_buf = background_path, key = KEY, start = start, stop = stop)
    df_len = df.shape[0]
    # current index to get background from
    subset_index = 0

    while(len(foregroundFiles) > 0): 

            # if should open a new foreground file
            if len(foreground_lines) <= 0:
                # reset the time stamp for the background packets
                prev_time   = 0
                df_index = random.randint(0, df_len-1)
                print("---------------------------------------------------------------")
                print("new file ", os.path.basename(foregroundFiles[0]))
                print("")

                # get the values (lines) of the new foreground file
                currForegroundFile = open(foregroundFiles[0], 'r') 
                foreground_lines   = currForegroundFile.readlines()
                currForegroundFile.close()
                foregroundFiles.pop(0)

                # open the merged file, that the result will be stored to
                currMergedFile = open(mergedFiles[0], 'a')
                mergedFiles.pop(0)

            # If the current web traffic packet is empty, one is at the end of the foreground file
            try:
                foreground_packet = foreground_lines[0].split(",")
            except:
                print("foreground file is empty, skip it")
                continue

            # timestamp the current background packet is on
            curr_time = prev_time + int(df.iat[df_index, TIME_INDEX])

            # add the packet that arrives first
            if(curr_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                currMergedFile.writelines([str(background_deviated_time), ",", str(df.iat[df_index, DIRECTION_INDEX]), ",", str(df.iat[df_index, SIZE_INDEX]), "\n"])
                prev_time = curr_time
                df_index += 1
                # if end of the background list, loop it from the start
                if df_index >= df_len:
                    df_index = 0
            else:
                currMergedFile.writelines(foreground_lines[0])
                foreground_lines.pop(0)
        
    return True

if __name__=="__main__":
    main()