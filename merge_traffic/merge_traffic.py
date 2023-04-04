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
This program merges the chosen foreground and background traffic

input:
    mergedFiles:     list of merged files
    foregroundFiles: list of foreground files
    background_path: path to the directory where the background files are be stored
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
    chunk = 1000
    
    # inject each foreground file
    for foregroundFile in foregroundFiles:
        print("---------------------------------------------------------------")
        print("new file ", os.path.basename(foregroundFile))
        print("")
        start_time = timeit.default_timer()
        # get the values (lines) of the new foreground file
        currForegroundFile = open(foregroundFile, 'r') 
        foregroundLines   = currForegroundFile.readlines()
        currForegroundFile.close()
        # open the merged file, that the result will be stored to
        currMergedFile = open(mergedFiles[0], 'a')
        mergedFiles.pop(0)

        # Prepare background for the foreground
        prev_pkt_time = 0
        index_df      = random.randint(start, stop-1)

        while len(foregroundLines) > 0:

            # extract a chunk or less of background packets
            if index_df + chunk < stop:
                curr_end = index_df + chunk
            else:
                curr_end = stop
            sub_df = df.iloc[index_df:curr_end]
            
            for row in sub_df.itertuples():
                # stop add background if the foreground list is empty
                if len(foregroundLines) <= 0:
                    break
                # timestamp the current background packet is on
                pkt_time = prev_pkt_time + int(row[TIME_INDEX])
                added_foreground =  False
                # Add background traffic, until one has added the foreground packet
                while(added_foreground == False):
                    # If the current web traffic packet is empty, one is at the end of the foreground file
                    try:
                        foreground_packet = foregroundLines[0].split(",")
                    except:
                        print("could not split foreground line")
                        break
                    # add the packet that arrives first
                    if(pkt_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                        currMergedFile.writelines(
                            [str(pkt_time), ",", 
                            str(row[DIRECTION_INDEX]), ",", 
                            str(row[SIZE_INDEX]), "\n"])

                        prev_pkt_time = pkt_time
                        added_foreground = False
                    else:
                        currMergedFile.writelines(foregroundLines[0])
                        foregroundLines.pop(0)
                        print("Added foreground")
                        added_foreground =  True

            # if need more background packets for this foreground file
            # start from the next chunk, or from the start
            if (curr_end + 1) < stop - 100:
                index_df = curr_end + 1
            else:
                index_df = start


        stop_time = timeit.default_timer()
        print('Time for the file: ', stop_time - start_time) 
        
    return True

if __name__=="__main__":
    main()