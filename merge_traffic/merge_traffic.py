#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/generate_merged_dataset/main.py
'''

import random
import pandas as pd
import os

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
    False:  it did not succeed
'''
def mergeTraffic(mergedFiles, foregroundFiles, background_path, start, stop):

    print("Start merging subset (takes a while to move background to memory)")

    # access the foreground packets time
    PACKET_ATTR_INDEX_TIME = 0
    # to access the background data
    KEY = "df"
    # index to access the values for the background packages
    TIME_INDEX      = 1
    DIRECTION_INDEX = 2
    SIZE_INDEX      = 3 
    
    # all lines in the open foreground file
    foreground_lines = []
    # timestamp of the current background packets, reset for each foreground file
    time_stamp = 0
    # the background traffic
    df = pd.read_hdf(background_path, key = KEY)
    
    # inject each foreground file
    for foregroundFile in foregroundFiles:
        print("---------------------------------------------------------------")
        print("new file ", os.path.basename(foregroundFile))
        print("")

        # get the values (lines) of the new foreground file
        currForegroundFile = open(foregroundFile, 'r') 
        foregroundLines   = currForegroundFile.readlines()
        currForegroundFile.close()
        # open the merged file, that the result will be stored to
        currMergedFile = open(mergedFiles[0], 'a')
        mergedFiles.pop(0)

        # Prepare background for the foreground
        time_stamp = 0
        index_df = random.randint(start, stop-1)
        sub_df = df.iloc[index_df:stop]
        rows = list(sub_df.itertuples())

        # inject all foreground lines
        for foregroundLine in foregroundLines:
            print("New foreground line")
            added_foreground =  False

            # Add background traffic, until one has added the foreground packet
            while(added_foreground == False):
                # timestamp the current background packet is on
                background_deviated_time = time_stamp + int(rows[0][TIME_INDEX])
                print("background dev time " + str(background_deviated_time))

                # If the current web traffic packet is empty, one is at the end of the foreground file
                try:
                    foreground_packet = foregroundLine.split(",")
                except:
                    added_foreground = True
                    print("foreground file is empty")
                    continue

                # add the packet that arrives first
                if(background_deviated_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                    currMergedFile.writelines(
                        [str(background_deviated_time), ",", 
                        str(rows[0][DIRECTION_INDEX]), ",", 
                        str(rows[0][SIZE_INDEX]), "\n"])
                    # next row in the list, of the list becomes empty, get packet from the start
                    rows.pop(0)
                    if len(rows) >= 0:
                        sub_df = df.iloc[0:stop]
                        rows = list(sub_df.itertuples())

                    time_stamp = background_deviated_time
                    added_foreground = False
                    print("Added background file")
                else:
                    currMergedFile.writelines(foregroundLine)
                    added_foreground =  True
                    print("Added foreground line")
        
    return True

if __name__=="__main__":
    main()