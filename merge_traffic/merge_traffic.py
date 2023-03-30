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
    False: it did not succeed
'''
def mergeTraffic(mergedFiles, foregroundFiles, background_path, start, stop):

    print("Start merging subset")

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
    # timestamp of the current background packets
    time_stamp = 0
    print("before df")
    # the background traffic
    df = pd.read_hdf(background_path, key = KEY)
    print("after df")
    # how many packets to use in a row before randomizing a packet again
    chunk = 100
    
    print("Start while loop")
    # add background traffic, until the foreground traffic is filled
    while(len(foregroundFiles) > 0): 

        # get randomized subset of the background to use
        rnd       = random.randint(start, stop-chunk)
        subset_df = df.isin(([rnd, rnd + chunk]))

        print(subset_df.size)
        return False

        print("Start for loop")
        # for every packet in the chunk of background traffic
        for row in subset_df.itertuples():

            # stop adding background traffic, when the foreground traffic is empty
            if len(foregroundFiles) <= 0:
                return True

            # Check if a new foreground file needs to be opened (which also imply a new merged should be opened)
            if len(foreground_lines) <= 0:
                print("Get a new foreground and merged file")
                # reset the time stamp for the background packets
                time_stamp = 0

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

            # timestamp the current background packet is on
            background_deviated_time = time_stamp + int(row[TIME_INDEX])
   
            # Add foreground traffic, until one has added the background traffic (or there is no more foreground traffic in this file)
            added_background =  False
            while(added_background == False):
                # If the current web traffic packet is empty, one is at the end of the foreground file
                try:
                    foreground_packet = foreground_lines[0].split(",")
                except:
                    print("foreground file is empty, skip it")
                    added_background = True
                    continue
                # add the packet that arrives first
                if(background_deviated_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                    currMergedFile.writelines([str(background_deviated_time), ",", str(row[DIRECTION_INDEX]), ",", str(row[SIZE_INDEX]), "\n"])
                    time_stamp = background_deviated_time
                    added_background = True
                else:
                    currMergedFile.writelines(foreground_lines[0])
                    foreground_lines.pop(0)
                    added_background =  False
        
    return True

if __name__=="__main__":
    main()