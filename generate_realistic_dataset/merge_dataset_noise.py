#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

TODO: loop the extraction of background traffic (if stop is longer than the total lenght, set offset to 0, and start to offset)

mergedTestFiles: list of mergedTestFiles
foregroundTestFiles: list of foregroundTestFiles
background_path: path to the background PATH_BACKGROUND
offset: offsets to use for the offsets

python wf-attack-vpn/generate_realistic_dataset/main.py
'''

import pandas as pd
import os

def mergeDatasetNoise(mergedFiles, foregroundFiles, background_path, offset):

    SIZE_DF_IN_MEMORY = 1000000

    PACKET_ATTR_INDEX_TIME = 0
    
    # all lines in the open foreground file
    foreground_lines = []
    key = "df"

    # how large part of the 
    start = offset
    stop  = offset + SIZE_DF_IN_MEMORY
    # To standardize the time between the foreground and the background
    time_stamp = 0

    first = True

    while(len(foregroundFiles) > 0): 

        print("gathering a new chunk of background traffic")
        df = pd.read_hdf(background_path, key = key, start = start, stop = stop)

        #df.to_csv("tmp.csv", index = True)
        #return False

        if first:
            time_index = df.columns.get_loc('time')
            direction_index = df.columns.get_loc('direction')
            size_index = df.columns.get_loc('size')

            print("Time: " + str(time_index))
            print("dir: " + str(direction_index))
            print("size: " + str(size_index))

        first = False

        for row in df.itertuples():

            # stop adding background traffic, when the foreground traffic is empty
            if len(foregroundFiles) <= 0:
                return True

            
            # Check if a new foreground file needs to be opened (which also imply a new merged should be opened)
            if len(foreground_lines) <= 0:
                
                # reset the time stamp for the new foreground file
                time_stamp = 0

                print("---------------------------------------------------------------")
                print("Reading form a new file ", os.path.basename(foregroundFiles[0]))
                print("")
                print("Printing to new file ", os.path.basename(mergedFiles[0]))
                print("---------------------------------------------------------------")

                # get the values of the new foreground file
                foregroundFile = open(foregroundFiles[0], 'r') 
                foregroundFiles.pop(0)
                foreground_lines = foregroundFile.readlines()
                foregroundFile.close()

                # open the merged file, that the result will be stored to
                mergedFile = open(mergedFiles[0], 'a')

                mergedFiles.pop(0)


            background_deviated_time = time_stamp + int(row[time_index])
            #background_packet = [str(background_deviated_time), ",", row[direction_index], ",", row[size_index], "\n"]

            # If the current web traffic packet is empty, add the current noise packet
            # Indicates that one should switch to a new web traffic file, but before that, one should add the noise
            try:
                foreground_packet = foreground_lines[0].split(",")
            except:
                mergedFile.writelines([str(background_deviated_time), ",", str(row[direction_index]), ",", str(row[size_index]), "\n"])
                print("foreground file is empty, added the noise line")
                continue

             # Sort the noise and the web traffic after time
            if(background_deviated_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                mergedFile.writelines([str(background_deviated_time), ",", str(row[direction_index]), ",", str(row[size_index]), "\n"])
                print("Added background")
            else:
                mergedFile.writelines(foreground_lines[0])
                foreground_lines.pop(0)
                print("Added foreground")
            

        # prepare next chunk of background traffic
        start = stop + 1
        stop = start + SIZE_DF_IN_MEMORY

    return True

if __name__=="__main__":
    main()