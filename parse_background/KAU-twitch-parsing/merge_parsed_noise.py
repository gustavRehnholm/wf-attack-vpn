#!/usr/bin/python3

'''
To run
python wf-attack-vpn/parse_background/KAU-twitch-parsing/merge_parsed_noise.py
'''

import pandas as pd
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input" , required = False , default = "twitch/parsed_captures/", type = str, help = "Directory for the parsed files")
ap.add_argument("--output", required = False , default = "background_traffic"     , type = str, help = "Directory to store the result")
ap.add_argument("--fname" , required = False , default = "twitch"                 , type = str, help = "file name for the result")
ap.add_argument("--start" , required = False , default = 0                        , type = int, help = "start index")
ap.add_argument("--stop"  , required = False , default = -1                       , type = int, help = "end index, -1 to use them all")
args = vars(ap.parse_args())


def main():
    merge_parsed_noise(dir_input   = args['input'],
                       dir_output  = args['output'],
                       fname       = args['fname'],
                       start_index = args['start'],
                       stop_index  = args['stop'])
    return


def merge_parsed_noise(dir_input = "twitch/parsed_captures/", dir_output = "background_traffic", fname = "twitch", start_index = 0, stop_index = 0):
    '''
    Merge all the parsed captures to one single file, where the timestamps flows logical between them
    Args:
        dir_input   - Optional : Directory for the parsed files (str)
        dir_output  - Optional : Directory to store the result  (str)
        fname       - Optional : file name for the result       (str)
        start_index - Optional : start index                    (int)
        stop_index  - Optional : end index, 0 to use them all   (int)
    '''

    print("Start merging the twitch captures")

    FILE_OUTPUT = fname + ".h5"
    PATH_OUTPUT = dir_output + "/" + FILE_OUTPUT
    COL_NAMES =  ['time', 'direction', 'size']
    # for storing the result as h5
    KEY = "df"
    index = 0
    df_merged = pd.DataFrame(columns = COL_NAMES)

    # clean the previous result
    os.system("rm " + PATH_OUTPUT)

    # list of all twitch traffic captures files
    files = os.listdir(dir_input)

    # Sort list of file names by size (only the 50 largest files)
    sorted_files = sorted(files, key =  lambda x: os.stat(os.path.join(dir_input, x)).st_size)
    sorted_files = list(reversed(sorted_files))
    if stop_index != 0:
        sorted_files = sorted_files[start_index:stop_index]
    else:
        sorted_files = sorted_files[start_index:]
    files_len    = len(sorted_files)


    # create the file, that the final result will be stored in
    # format table, so that it is appendable
    merged_df = pd.DataFrame(columns = COL_NAMES)
    merged_df.to_hdf(PATH_OUTPUT, mode = "w", key = KEY, format = 'table') 

    for file in sorted_files:
        index += 1
        filename = os.fsdecode(file)

        print("")
        print("merging file " + str(index) + "/" + str(files_len) + ": " + str(filename))
        print("")

        path = dir_input + filename
        df = pd.read_hdf(path, key = KEY)
        df.to_hdf(PATH_OUTPUT, mode = "r+", key = KEY, append = True) 

    print("Have merged all twitch traffic, store them now in " + PATH_OUTPUT)

if __name__=="__main__":
    main()