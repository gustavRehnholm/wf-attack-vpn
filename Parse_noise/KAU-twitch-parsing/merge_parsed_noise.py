#!/usr/bin/python3

'''
Merge all the parsed captures to one single file, where the timestamps flows logical between them

touch stdout/merge_parsed_noise.py
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/merge_parsed_noise.py | tee stdout/merge_parsed_noise.py
'''

import pandas as pd
import os

def main():
    print("Start merging the twitch captures")

    # the csv files 
    DIR_INPUT = "twitch/parsed_captures/"
    # the merged noise file in the h5 format
    DIR_OUTPUT = "twitch/merged_captures/"
    # for storing the result as h5
    key = "df"
    index = 0
    df_merged = pd.DataFrame(columns = ['time', 'direction', 'size'])

    COL_NAMES =  ['time', 'direction', 'size']


    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    # to correct each captures time, so they all follow a chronological order
    deviation_time = 0

    # list of all twitch traffic cpatures files
    files = os.listdir(DIR_INPUT)
    files.sort()

    # create the file, that the rest will append to
    merged_df = pd.DataFrame(columns = COL_NAMES)
    MERGED_FILE_NAME = DIR_OUTPUT + 'twitch.h5'
    merged_df.to_hdf(MERGED_FILE_NAME, mode = "w", key = "df") 

    for file in files:
        index += 1
        filename = os.fsdecode(file)
        
        print("")
        print("merging file " + str(index) + "/1362: " + str(filename))
        print("")

        path = DIR_INPUT + filename
        df = pd.read_hdf(path, key=key)
        # time corrections on the timeframes
        for i, row in df.iterrows():
            row["time"] =  row["time"] + deviation_time

        # to shift each new capture forward in time
        deviation_time = df['time'].iloc[-1]

        # append current files result to the final result file
        df.to_hdf(MERGED_FILE_NAME, mode = "a", key = "df") 


    print("Have merged all twitch traffic, store them now in " + MERGED_FILE_NAME)
    


# run main 
if __name__=="__main__":
    main()