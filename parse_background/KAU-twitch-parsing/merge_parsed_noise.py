#!/usr/bin/python3

import pandas as pd
import os

'''
python wf-attack-vpn/parse_background/KAU-twitch-parsing/merge_parsed_noise.py
'''

def main():
    '''
    Merge all the parsed captures to one single file, where the timestamps flows logical between them
    '''

    print("Start merging the twitch captures")

    # the csv files 
    DIR_INPUT = "twitch/parsed_captures/"
    # the merged noise file in the h5 format
    DIR_OUTPUT = "background_traffic"
    # [40,80[
    # twitch_40
    # twitch_1_first
    # twitch_1_last
    # twitch_1_middle
    FILE_OUTPUT = "twitch_1_first.h5"
    PATH_OUTPUT = DIR_OUTPUT + "/" + FILE_OUTPUT
    COL_NAMES =  ['time', 'direction', 'size']
    # for storing the result as h5
    key = "df"
    index = 0
    df_merged = pd.DataFrame(columns = COL_NAMES)

    # clean the previous result
    os.system("mkdir " + DIR_OUTPUT)
    os.system("rm " + PATH_OUTPUT)
    
    # to correct each captures time, so they all follow a chronological order
    deviation_time = 0

    # list of all twitch traffic captures files
    files = os.listdir(DIR_INPUT)
    #files.sort()

    # Sort list of file names by size (only the 50 largest files)
    sorted_files = sorted(files, key =  lambda x: os.stat(os.path.join(DIR_INPUT, x)).st_size)
    sorted_files = list(reversed(sorted_files))
    files_len    = len(sorted_files)

    # create the file, that the final result will be stored in
    # format table, so that it is appendable
    merged_df = pd.DataFrame(columns = COL_NAMES)
    merged_df.to_hdf(PATH_OUTPUT, mode = "w", key = key, format = 'table') 

     #sorted_files.reverse()

    for file in sorted_files:
        index += 1
        filename = os.fsdecode(file)

        if index == 40:
        #if index == 80:
        #if index == 60:
        #if index >= 40 and index < 80:
        
            print("")
            print("merging file " + str(index) + "/" + str(files_len) + ": " + str(filename))
            print("")

            path = DIR_INPUT + filename
            df = pd.read_hdf(path, key=key)
            df.to_hdf(PATH_OUTPUT, mode = "r+", key = key, append = True) 
            
        if index >= 80:
            print("Have merged all twitch traffic, store them now in " + PATH_OUTPUT)
            return

    print("Have merged all twitch traffic, store them now in " + PATH_OUTPUT)

# run main 
if __name__=="__main__":
    main()