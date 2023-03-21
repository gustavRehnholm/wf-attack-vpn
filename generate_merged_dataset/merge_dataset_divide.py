#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

input:
    mergedFiles: list of paths to the merged files
    foregroundFiles: list of paths to the foreground files
    background_path: list of paths to the background files
    offset: offsets the start packet of the background files
    chunk: how large dataset to have in memory at a time
    background_amount: [0, 1] how large part of the background traffic should be used
output:
    True: it succeeded in creating the whole merged files
    False: it did not succeed

python wf-attack-vpn/generate_merged_dataset/main.py
'''

import pandas as pd
import os

def mergeDatasetNoiseDivide(mergedFiles, foregroundFiles, background_path, background_start, background_stop, chunk, background_amount = 1):
    print("Start merge, with divided set, iterative")
    if not isinstance(background_start, int):
        print("must start with an integer")
        print(type(background_start))
        return False
    if not isinstance(background_stop, int):
        print("must end with an integer")
        print(type(background_stop))
        return False
    if not isinstance(chunk, int):
        print("chunk must be an integet")
        print(type(chunk))
        return False

    # how many packets of background traffic to have in memory at a time
    CHUNK = chunk
    # access the foreground packets time
    PACKET_ATTR_INDEX_TIME = 0
    
    # all lines in the open foreground file
    foreground_lines = []
    # to access the background data
    key = "df"
    # timestamp of the current background packets
    time_stamp = 0
    # index to access the values for the background packages
    time_index      = 1
    direction_index = 2
    size_index      = 3 
    # how large part of the background to have in the memory at a time
    start = background_start
    stop  = background_start + CHUNK
    # if stop is to large, set it to the last index
    if stop > background_stop:
        stop = background_stop
    
    # add background traffic, until the foreground traffic is filled
    while(len(foregroundFiles) > 0): 

        df = pd.read_hdf(background_path, key = key, start = start, stop = stop)

        # for every packet in the chunk of background traffic
        for row in df.itertuples():

            # stop adding background traffic, when the foreground traffic is empty
            if len(foregroundFiles) <= 0:
                return True

            # Check if a new foreground file needs to be opened (which also imply a new merged should be opened)
            if len(foreground_lines) <= 0:
                
                # reset the time stamp for the background packets
                time_stamp = 0

                print("---------------------------------------------------------------")
                print("new file ", os.path.basename(foregroundFiles[0]))
                print("")

                # get the values of the new foreground file
                foregroundFile = open(foregroundFiles[0], 'r') 
                foregroundFiles.pop(0)
                foreground_lines = foregroundFile.readlines()
                foregroundFile.close()

                # open the merged file, that the result will be stored to
                mergedFile = open(mergedFiles[0], 'a')
                mergedFiles.pop(0)

            # timestamp the current background packet is on
            background_deviated_time = time_stamp + int(row[time_index])
   
            added_background =  False
             # Add foreground traffic, until one has added the background traffic (or there is no more foreground traffic in this file)
            while(added_background == False):
                # If the current web traffic packet is empty, one is at the end of the foreground file
                try:
                    foreground_packet = foreground_lines[0].split(",")
                except:
                    #print("foreground file is empty, skip it")
                    added_background = True
                    continue
                # add the packet that arrives first
                if(background_deviated_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                    mergedFile.writelines([str(background_deviated_time), ",", str(row[direction_index]), ",", str(row[size_index]), "\n"])
                    time_stamp = background_deviated_time
                    added_background = True
                else:
                    mergedFile.writelines(foreground_lines[0])
                    foreground_lines.pop(0)
                    added_background =  False

        # prepare next chunk of background traffic
        start = stop + 1
        stop = start + CHUNK
        
        # if start is beyond the size, get chunk from the start again
        if start >= background_stop:
            print("Loop the background noise")
            start = background_start
            stop  = CHUNK
        # if stop is to long, set it to the end of the list (will loop the list next iteration)
        elif stop > background_stop:
            print("Last chunk before the loop")
            stop = background_stop
        
    return True

if __name__=="__main__":
    main()