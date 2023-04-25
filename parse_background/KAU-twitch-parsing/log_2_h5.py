#!/usr/bin/python3

import pandas as pd
import os
import sys
from multiprocessing import Pool
import timeit
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-w"     , required = False, default = 10 , type = int, help = "number of workers (multiprocessing)")
args = vars(ap.parse_args())

'''
TODO: progressbar
'''

def log_2_h5(dir_input = "captures/", dir_output = "twitch/raw_captures_h5/"):
    '''
    Convert the raw log files to dataframes, and store them with h5
    That way, they will be faster to handle

    Args:
        dir_input  - Optional : Path to the raw log files from rds-collect      (str)
        dir_output - Optional : Path where the converted dataset will be stored (str)
    '''

    print("Start converting twitch traffic")

    COL_NAMES =  ['time', 'sender_receiver', 'size']


    # clean old results if their is any
    if os.path.exists(dir_output):
        shutil.rmtree(dir_output)
    os.mkdir(dir_output)

    input = []
    files = os.listdir(dir_input)
    for curr_file in files:
        input.append((dir_input, dir_output, curr_file, COL_NAMES))
    len_files = len(input)

    start_time = timeit.default_timer()
    p = Pool(args['w'])
    p.starmap(convert_2_hdf5, input)

    end_time = timeit.default_timer()
    print(f"runtime for converting the data: {end_time - start_time}")
    return


def convert_2_hdf5(dir_input, dir_output, file, col_names):
    '''
    convert the provided log file to an hdf5 file

    Args:
        dir_input  - Required : where the log file is stored          (str)
        dir_output - Required : where the hdf5 file should be stored  (str)
        file       - Required : file to convert                       (str)
        col_names  - Required : name of the columns for the hdf5 file (List[str])
    '''
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