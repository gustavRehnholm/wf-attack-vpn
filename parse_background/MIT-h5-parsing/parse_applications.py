#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/parse_background/MIT-h5-parsing/parse_applications.py -w 1
'''

import os
import argparse
import pandas as pd
from multiprocessing import Pool

ap = argparse.ArgumentParser()
ap.add_argument("-w"     , required = False, default = 10 , type = int, help = "number of workers (multiprocessing)")
args = vars(ap.parse_args())

def main():
    '''
    To run parse_applications individual from the terminal
    '''
    parse_applications(workers = args['w'])
    return


def parse_applications(workers = 10):
    '''
    Parse all the extracted MIT application datasets
    '''

    DIR_INPUT  = "mit/raw_app"
    DIR_OUTPUT = "mit/parsed_app"
    pool_input = []

    for app_file in os.listdir(DIR_INPUT):
        path_in  = f"{DIR_INPUT}/{app_file}"
        path_out = f"{DIR_OUTPUT}/{app_file}" 
        parse_file(path_in, path_out)
        #pool_input.append((path_in, path_out))

    #p = Pool(workers)
    #p.starmap(parse_file, pool_input)

    return


def parse_file(input_path, output_path):
    '''
    parse hdf5 file for one applications, so it goes to:
    * one row per packet
    * Sec to NS
    * absolute time to relative time
    * direction from 1 and 0, to "sb" and "rb"

    Args:
        input_path  - Required : path to the file to parse (str)
        output_path - Required : path for the result       (str)
    '''
    NS_PER_SEC = 1000000000

    dictionary_parsed = {
        'time'     : [],
        'direction': [],
        'size'     : []
    }

    df = pd.read_hdf(input_path)

    all_captures = []
    
    # each row is an capture
    for index, row in df.iterrows():
        all_captures.append((df['timestamps'], df['sizes'], df['directions']))

        '''

        timestamps = df['timestamps']
        sizes      = df['sizes']
        directions = df['directions']

        nr_of_timestamps = len(df['timestamps'])
        nr_of_sizes      = len(df['sizes'])
        nr_of_directions = len(df['directions'])

        if nr_of_timestamps != nr_of_directions != nr_of_sizes:
            print("ERROR: there is not equal amount of timestamps and directions")
            print(f"{input_path}: nr of timestamps: {nr_of_timestamps}, nr of directions: {nr_of_directions}, nr of directions: {nr_of_sizes}")
            return
        elif nr_of_timestamps < 1:
            print(f"ERROR: the number of timestamps to is small {nr_of_timestamps}")
            return

        all_captures.append((timestamps, sizes, directions))
        '''
    # parse each capture
    for capture in all_captures:
        # reset start time for each capture file
        prev_time = capture[0][0] * NS_PER_SEC
        # parse each pkt for each capture
        for i in range(len(capture[0])):
            # get the time
            absolute_time = capture[0][i] * NS_PER_SEC
            relative_time = round(absolute_time - prev_time)
            prev_time     = absolute_time
            if relative_time == 0:
                relative_time = 1
            elif relative_time < 0:
                print("ERROR: duration is negative")

            # get the size
            size = capture[1][i]

            raw_dir = capture[2][i]
            # get the direction
            if raw_dir == 1:
                direction = "sb"
            elif raw_dir == 0:
                direction = "rb"
            else:
                print(f"ERROR: direction {raw_dir} is invalid")
            

            dictionary_parsed['time'].append(relative_time)
            dictionary_parsed['direction'].append(direction)
            dictionary_parsed['size'].append(size)

    # save the result
    df_parsed = pd.DataFrame(dictionary_parsed)
    df_parsed.to_hdf(output_path, mode = "w", key = "df") 


if __name__=="__main__":
    main()