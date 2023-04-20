#!/usr/bin/python3

import pandas as pd
import os
import sys
from multiprocessing import Pool

def main():
    '''
    Convert the raw log files to dataframes, and store them with h5
    That way, they will be faster to handle
    '''

    print("Start converting twitch traffic")

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    files = os.listdir(DIR_INPUT)
    len_files = len(files)

    p = Pool(10)
    p.starmap(convert_2_hdf5, files)

def convert_2_hdf5(file):
    filename = os.fsdecode(file)
    if not filename.endswith(".log"): 
        print("ERROR: the file (" + str(filename) + ") should not be part of the directory")
        print("Only log files should be part of the twitch dataset")
        print("Aborting the program")
        sys.exit()

    COL_NAMES =  ['time', 'sender_receiver', 'size']
    # parsed noise files
    DIR_INPUT = "captures/"
    # the captures in h5 format
    DIR_OUTPUT = "twitch/raw_captures_h5/"
    key = "df"

    path = DIR_INPUT + filename
    df = pd.read_csv(path, names = COL_NAMES, delim_whitespace = True)

    df_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.h5'
    df.to_hdf(df_file_name, mode = "w", key = key)

# run main 
if __name__=="__main__":
    main()