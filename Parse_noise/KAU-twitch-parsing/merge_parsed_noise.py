#!/usr/bin/python3

'''
Merge all the parsed captures to one single file, where the timestamps flows logical between them

touch stdout/merge_parsed_noise.py
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/merge_parsed_noise.py | tee stdout/merge_parsed_noise.py
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/merge_parsed_noise.py
'''

import pandas as pd
import os

def main():
    print("Start merging the twitch captures")

    # the csv files 
    DIR_INPUT = "twitch/parsed_captures/"
    # the merged noise file in the h5 format
    DIR_OUTPUT = "background_traffic"
    FILE_OUTPUT = "twitch.h5"
    PATH_OUTPUT = DIR_OUTPUT + "/" + FILE_OUTPUT
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

    # list of all twitch traffic captures files
    files = os.listdir(DIR_INPUT)
    files.sort()

    # create the file, that the final result will be stored in
    merged_df = pd.DataFrame(columns = COL_NAMES)
    
    merged_df.to_hdf(PATH_OUTPUT, mode = "w", key = key) 

    first = True

    for file in files:
        index += 1
        filename = os.fsdecode(file)
        
        print("")
        print("merging file " + str(index) + "/1362: " + str(filename))
        print("")

        path = DIR_INPUT + filename
        df = pd.read_hdf(path, key=key)

        # append current files result to the final result file
        df.to_hdf(PATH_OUTPUT, mode = "a", key = key) 


    print("Have merged all twitch traffic, store them now in " + PATH_OUTPUT)

# run main 
if __name__=="__main__":
    main()