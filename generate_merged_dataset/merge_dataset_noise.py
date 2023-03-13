#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

TODO: loop the extraction of background traffic (if stop is longer than the total lenght, set offset to 0, and start to offset)

TODO: check why does it loops the same data???

mergedTestFiles: list of mergedTestFiles
foregroundTestFiles: list of foregroundTestFiles
background_path: path to the background PATH_BACKGROUND
offset: offsets to use for the offsets

python wf-attack-vpn/generate_merged_dataset/main.py
'''

import pandas as pd
import os

def mergeDatasetNoise(mergedFiles, foregroundFiles, background_path, offset_percent, chunk):

    CHUNK = chunk
    PACKET_ATTR_INDEX_TIME = 0
    
    # all lines in the open foreground file
    foreground_lines = []
    key = "df"


    # To standardize the time between the foreground and the background
    time_stamp = 0

    time_index      = 1
    direction_index = 2
    size_index      = 3 

    # get size of the background traffic
    store = pd.HDFStore(background_path)
    df_len = store.get_storer(key).nrows
    store.close()

    offset = int(df_len * offset_percent)
    # how large part of the 
    start = offset
    stop  = offset + CHUNK
    
    # add background traffic, until the foreground traffic is filled
    while(len(foregroundFiles) > 0): 

        #print("gathering a new chunk of background traffic")
        df = pd.read_hdf(background_path, key = key, start = start, stop = stop)
        '''
        try:
            df = pd.read_hdf(background_path, key = key, start = start, stop = stop)
        except:
            print("Loop the background noise")
            start = 0
            stop = CHUNK
            df = pd.read_hdf(background_path, key = key, start = start, stop = stop)
        '''

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

            # If the current web traffic packet is empty, add the current noise packet
            # Indicates that one should switch to a new web traffic file, but before that, one should add the noise
            try:
                foreground_packet = foreground_lines[0].split(",")
            except:
                mergedFile.writelines([str(background_deviated_time), ",", str(row[direction_index]), ",", str(row[size_index]), "\n"])
                time_stamp = background_deviated_time
                print("foreground file is empty, added the noise line")
                continue
            
             # Sort the noise and the web traffic after time
            if(background_deviated_time < int(foreground_packet[PACKET_ATTR_INDEX_TIME])):
                mergedFile.writelines([str(background_deviated_time), ",", str(row[direction_index]), ",", str(row[size_index]), "\n"])
                time_stamp = background_deviated_time
            else:
                mergedFile.writelines(foreground_lines[0])
                foreground_lines.pop(0)
            

        # prepare next chunk of background traffic
        start = stop + 1
        stop = start + CHUNK
        
        # if stop is beyond the length of the data, loop around
        if stop >= df_len:
            print("Loop the background noise")
            start = 0
            stop  = CHUNK
        
    return True

if __name__=="__main__":
    main()