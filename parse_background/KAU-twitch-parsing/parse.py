#!/usr/bin/python3

import pandas as pd
import os
from multiprocessing import Pool
import timeit

# the usable captures
DIR_INPUT = "twitch/usable_captures_h5/"
# for the parsed captures
DIR_OUTPUT = "twitch/parsed_captures/"
# 1000000000 ns = 1 sec
NANO_SEC_PER_SEC = 1000000000
# How much of the header to remove (to fit the noise with the web traffic)
HEADER = 40
# for storing the result as h5
KEY = "df"
time_index            = 1
sender_receiver_index = 2
size_index            = 3

df_columns = ['time', 'direction', 'size']

def main():
    '''
    Parse the twitch noise, which is converted to dataframes in the h5 format

    Assumption:
    that the captured data starts its captures from the time 0

    Takes a little while to run, good time to grab a cup with coffee
    TODO: implement multiprocessor to speed it up 
    '''

    print("Start generating parsing")


    # is used to get the direction of each packet
    ipHost = '10.88.0.9'

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    # the capture files that will be parsed
    input_files = os.listdir(DIR_INPUT)
    input_files.sort()
    

    input = []
    for curr_file in input_files:
        input.append((curr_file, ipHost))

    start_time = timeit.default_timer()
    p = Pool(10)
    p.starmap(parse_file, input)

    end_time = timeit.default_timer()
    print(f"runtime for parsing (sec): {end_time - start_time}")

    print("Have saved the parsed results, ending the program")

    return


def parse_file(file, ipHost):
    # should start at 0 for each file
    prev_time = 0
    # to store the parsed file
    df_parsed = pd.DataFrame(columns = df_columns)
    # Dictionary to append the results for each row for a file
    dictionary_parsed = {
        'time': [],
        'direction': [],
        'size': []
    }

    filename = os.fsdecode(file)
    # get the data from the current file
    path = DIR_INPUT + filename
    df_unsorted   = pd.read_hdf(path, key=KEY)

    df = df_unsorted.sort_values(by='time')

    capture_len = 0
    for row in df.itertuples():
        capture_len += 1
        # flag to check if the packet is broken, so it can be skipped
        broken = False

        # convert from timestamp in sec, to duration form last packet in ns
        if not row[time_index]:
            broken = True
            continue
        else:
            # get the duration (in ns) between this packet, and the one before it
            parsed_time_float_sec = row[time_index] - prev_time
            parsed_time_float_ns  = parsed_time_float_sec * NANO_SEC_PER_SEC
            parsed_time           = round(parsed_time_float_ns)

            # Some packets are in the wrong order, 
            if parsed_time < 0:
                broken = True
                continue
            elif parsed_time == 0:
                parsed_time = 1

        sender_receiver = str(row[sender_receiver_index]).split(",")
        # if no or only one IP address, skip this packet
        if len(sender_receiver) < 2:
            broken = True
            continue
        else:
            sender          = sender_receiver[0]
            receiver        = sender_receiver[1]

            # get direction
            if sender == "":
                broken = True
                continue
            elif sender == ipHost:
                parsed_direction = "sb"
            elif receiver == ipHost:
                parsed_direction = "rb"
            else:
                sender_start_ip = sender.split('.')
                if sender_start_ip[0] == '10':
                    ipHost = sender_start_ip[0]
                    parsed_direction = "sb"
                else:
                    ipHost = sender_start_ip[1]
                    parsed_direction = "rb"

        # get size
        try:
            parsed_size = int(row[size_index]) - HEADER
        except:
            broken = True
            continue

        if parsed_size <= 0:
            broken = True
            continue

        if not broken:
            dictionary_parsed['time'].append(parsed_time)
            dictionary_parsed['direction'].append(parsed_direction)
            dictionary_parsed['size'].append(parsed_size)

            # update time for the packet before (in sec as float)
            prev_time = row[time_index]

    # have parsed the whole file, store the result
    df_parsed = pd.DataFrame(dictionary_parsed)

    df_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.h5'
    df_parsed.to_hdf(df_file_name, mode = "w", key = KEY) 

    return


# run main 
if __name__=="__main__":
    main()