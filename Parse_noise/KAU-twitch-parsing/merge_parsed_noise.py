#!/usr/bin/python3

'''
Merge all the parsed captures to one single file, where the timestamps flows logical between them

touch stdout/merge_parsed_noise.py
python wf-attack-vpn/KAU-twitch-parsing/merge_parsed_noise.py | tee stdout/merge_parsed_noise.py
'''

import pandas as pd
import os

def main():
    print("Start merging the twitch captures")

    # the csv files 
    DIR_PARSED_NOISE = "twitch/parsed_captures/"
    # the merged noise file in the h5 format
    DIR_MERGED_NOISE = "twitch/merged_captures/"
    # for storing the result as h5
    key = "df"
    index = 0
    df_merged = pd.DataFrame(columns = ['time', 'direction', 'size'])

    COL_NAMES =  ['time', 'direction', 'size']

    # to correct each captures time, so they all follow a chronological order
    deviation_time = 0

    merged_df = pd.DataFrame(columns = COL_NAMES)

    for file in os.listdir(DIR_PARSED_NOISE):
        index += 1
        filename = os.fsdecode(file)
        
        print("")
        print("merging file " + str(index) + "/1370: " + str(filename))
        print("")

        path = DIR_PARSED_NOISE + filename
        df = pd.read_hdf(path, key=key)
        # time corrections on the timeframes
        for i, row in df_file.iterrows():
            row["time"] =  row["time"] + deviation_time

        # to shift each new capture forward in time
        deviation_time = df_file['time'].iloc[-1]

        # add the capture with shifted time, to the df for the whole dataset
        merged_df = pd.concat([merged_df, df], axis=0)

    
    merged_file_name = DIR_MERGED_NOISE + 'twitch.h5'
    print("Have merged all twitch traffic, store them now in " + merged_file_name)
    df.to_hdf(merged_file_name, mode = "w", key = "df") 


# run main 
if __name__=="__main__":
    main()