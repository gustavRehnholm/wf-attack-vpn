#!/usr/bin/python3

'''
Merge all the parsed captures to one single file, where the timestamps flows logical between them
'''

import pandas as pd
import os

def main():
    print("Start merging the twitch captures")

    # the csv files 
    DIR_INPUT = "twitch/parsed_captures/"
    # the merged noise file in the h5 format
    DIR_OUTPUT = "background_traffic"
    FILE_OUTPUT = "twitch_1.h5"
    PATH_OUTPUT = DIR_OUTPUT + "/" + FILE_OUTPUT
    # for storing the result as h5
    key = "df"
    index = 0
    df_merged = pd.DataFrame(columns = ['time', 'direction', 'size'])

    COL_NAMES =  ['time', 'direction', 'size']


    # clean the previous result
    os.system("mkdir " + DIR_OUTPUT)
    os.system("rm " + PATH_OUTPUT)
    

    # to correct each captures time, so they all follow a chronological order
    deviation_time = 0

    # list of all twitch traffic captures files
    files = os.listdir(DIR_INPUT)
    files.sort()
    files_len = len(files)

    # create the file, that the final result will be stored in
    # format table, so that it is appendable
    merged_df = pd.DataFrame(columns = COL_NAMES)
    merged_df.to_hdf(PATH_OUTPUT, mode = "w", key = key, format = 'table') 

    first = True

    for file in files:
        index += 1
        filename = os.fsdecode(file)
        
        print("")
        print("merging file " + str(index) + "/" + str(files_len) + ": " + str(filename))
        print("")

        path = DIR_INPUT + filename
        df = pd.read_hdf(path, key=key)

        if filename == "tshark_1.9h_twitch-jackport99_stream_2023-01-04_1.h5":
            # append current files result to the final result file
            # append = True: the value should be appended on the old
            df.to_hdf(PATH_OUTPUT, mode = "r+", key = key, append = True) 
            print("Added the file")
            return

        # to gather a subset
        #if index >= 150:
        #    return


    print("Have merged all twitch traffic, store them now in " + PATH_OUTPUT)

# run main 
if __name__=="__main__":
    main()