#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

TODO: loop the extraction of background traffic (if stop is longer than the total lenght, set offset to 0, and start to offset)

mergedTestFiles: list of mergedTestFiles
foregroundTestFiles: list of foregroundTestFiles
background_path: path to the background PATH_BACKGROUND
offset: offsets to use for the offsets
'''

import pandas as pd

def mergeDatasetNoise(mergedFiles, foregroundFiles, background_path, offset):

    SIZE_DF_IN_MEMORY = 1000
    
    # all lines in the open foreground file
    foreground_lines = []

    # how large part of the 
    start = offset
    stop  = offset + SIZE_DF_IN_MEMORY
    # To standardize the time between the foreground and the background
    deviationTime = 0


    while(len(foregroundFiles) > 0): 

        df = pd.read_hdf(background_path, key = key, iterator=True, start = start, stop = stop)
        for row in df.itterows():
            # stop adding background traffic, when the foreground traffic is empty
            if len(foregroundFiles) <= 0:
                return True

            
            # Check if a new web traffic file needs to be loaded
            if len(webTrafficLines) <= 0:
                
                deviationTime = row['time'] 

                foregroundFile = open(foregroundFiles[0], 'r') 
                foregroundFiles.pop(0)
                foreground_lines = foregroundFile.readlines()
                foregroundFile.close()


            background_deviated_time = row['time'] - deviationTime
            background_packet = [str(background_deviated_time), ",", row['direction'], ",", row['size'], "\n"]

            # If the current web traffic packet is empty, add the current noise packet
            # Indicates that one should switch to a new web traffic file, but before that, one should add the noise
            try:
                foreground_packet = foreground_lines[0].split(",")
            except:
                mergedFiles.writelines(background_packet)
                # print("Crossline is empty, added the noise line")
                continue

             # Sort the noise and the web traffic after time
            if(background_deviated_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                mergedFiles.writelines(background_packet)
            else:
                mergedFiles.writelines(foreground_lines[0])
                foreground_lines.pop(0)

        # prepare next chunk of background traffic
        start = stop + 1
        stop = start + SIZE_DF_IN_MEMORY

    return True

if __name__=="__main__":
    main()