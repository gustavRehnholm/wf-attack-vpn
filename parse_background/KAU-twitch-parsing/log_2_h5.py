#!/usr/bin/python3

import pandas as pd
import os
import sys
from multiprocessing import Pool
import timeit



def main():
    '''
    Convert the raw log files to dataframes, and store them with h5
    That way, they will be faster to handle
    '''

    print("Start converting twitch traffic")

    COL_NAMES =  ['time', 'sender_receiver', 'size']
    # parsed noise files
    DIR_INPUT = "captures/"
    # the captures in h5 format
    DIR_OUTPUT = "twitch/raw_captures_h5/"

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    input = []
    files = os.listdir(DIR_INPUT)
    for curr_file in files:
        input.append((DIR_INPUT, curr_file, DIR_OUTPUT, COL_NAMES))
    len_files = len(input)

    start_time = timeit.default_timer()
    p = Pool(10)
    p.starmap(convert_2_hdf5, input)

    end_time = timeit.default_timer()
    print(f"runtime for converting the data: {end_time - start_time}")


def convert_2_hdf5(dir_input, dir_output, file, col_names):
    KEY = "df"
    filename = os.fsdecode(file)
    if not filename.endswith(".log"): 
        print("ERROR: the file (" + str(filename) + ") should not be part of the directory")
        print("Only log files should be part of the twitch dataset")
        print("Aborting the program")
        sys.exit()

    path = dir_input + filename
    df = pd.read_csv(path, names = col_names, delim_whitespace = True)

    df_file_name = dir_output + filename.rsplit('.', 1)[0] + '.h5'
    df.to_hdf(df_file_name, mode = "w", key = KEY)

    return

# run main 
if __name__=="__main__":
    main()