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

import random
import pandas as pd
import os

def mergeDatasetNoiseDivideRnd(mergedFiles, foregroundFiles, background_path, background_start, background_stop, chunk, background_amount = 1):

    if background_start is not int:
        print("must start with an integer, not " + background_start)
        return False
    if background_stop is not int:
        print("must end with an integer, not " + background_stop)
    if chunk is not int:
        print("chunk must be an integet, not " + chunk)
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

    # how many chunks there is in the background
    df_len = background_stop - background_start
    nr_of_chunks = int(df_len/chunk)
    # in the slim case that this would be real
    if nr_of_chunks == df_len/chunk:
        nr_of_chunks -= 1
        print("the background traffic was devisable on the chunk size, set it one less")
    
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
        # can be [0, nr_of_chunks]
        start_chunk = random.randint(0, nr_of_chunks)
        start = start_chunk * CHUNK + background_start
        stop = start + CHUNK 

        # incase there is an bug with the start position
        if start > background_stop:
            print("ERROR, start got to big!")
            return False
        # incase the stop went beyond the length
        if stop > background_stop:
            stop = background_stop
        
    return True

if __name__=="__main__":
    main()