#!/usr/bin/python3

'''
Parse the twitch noise, which is converted to dataframes in the h5 format

Assumption:
 that the captured data starts its captures from teh time 0, and that the time between the first packet and time 0, is representable for time between two packets

Takes a little while to run, good time to grab a cup with coffee
TODO: implement multiprocessor to speed it up 


To run, type the following in the terminal:

touch stdout/parse.txt

python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/parse.py | tee stdout/parse.txt
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/parse.py
'''

import pandas as pd
import os

def main():
    print("Start generating parsing")

    # the usable captures
    DIR_INPUT = "twitch/usable_captures_h5/"
    # for the parsed captures
    DIR_OUTPUT = "twitch/parsed_captures/"
    # 1000000000 ns = 1 sec
    NANO_SEC_PER_SEC = 1000000000
    # How much of the header to remove (to fit the noise with the web traffic)
    HEADER = 40

    # is used to get the direction of each packet
    ipHost = '10.88.0.9'
    # for storing the result as h5
    key = "df"

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    # the capture files that will be parsed
    input_files = os.listdir(DIR_INPUT)
    input_files.sort()

    # to inform the user how long the script has run
    curr_file_index = -1
    total_files = len(input_files)

    # for trouble shooting
    amount_in_wrong_order = [0] * total_files
    amount_with_zero = [0] * total_files
    
    # Dictionary to append the results for each row for a file
    dictionary_parsed = {
        'time': [],
        'direction': [],
        'size': []
    }
    # to store the parsed file
    df_parsed = pd.DataFrame(columns = ['time', 'direction', 'size'])

    time_index            = 1
    sender_receiver_index = 2
    size_index            = 3


    # loop thorugh all files, and use their values for the parsed result
    for file in input_files:

        # should start at 0 for each file
        prev_time = 0

        # clear the dictionary and the dataFrame
        df_parsed = df_parsed.iloc[0:0]
        dictionary_parsed.clear()
        dictionary_parsed = {
            'time': [],
            'direction': [],
            'size': []
        }

        curr_file_index += 1
        filename = os.fsdecode(file)
        print("")
        print("parsing file " + str(curr_file_index) + "/" + str(total_files) + ": " + str(filename))
        print("")

        # get the data from the current file
        path = DIR_INPUT + filename
        df_unsorted   = pd.read_hdf(path, key=key)

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
                    amount_in_wrong_order[curr_file_index] += 1
                    broken = True
                    continue
                elif parsed_time == 0:
                    parsed_time = 1
                    amount_with_zero[curr_file_index] += 1



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
                    parsed_direction = "s"
                elif receiver == ipHost:
                    parsed_direction = "r"
                else:
                    sender_start_ip = sender.split('.')
                    if sender_start_ip[0] == '10':
                        ipHost = sender_start_ip[0]
                        parsed_direction = "s"
                    else:
                        ipHost = sender_start_ip[1]
                        parsed_direction = "r"

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

        print("Done parsing the file " + str(filename))
        print("Out of " + str(capture_len) + "files:")
        print("the number of packets that was in the wrong order")
        print(amount_in_wrong_order[curr_file_index])
        print("the number of packets that was slower than 1 ns")
        print(amount_with_zero[curr_file_index])

        # have parsed the whole file, store the result
        df_parsed = pd.DataFrame(dictionary_parsed)

        df_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.h5'
        df_parsed.to_hdf(df_file_name, mode = "w", key = key) 


    amount_in_wrong_order.sort()
    amount_with_zero.sort()
    print("Shows the 10 worst cases of: ")
    print("the number of packets that was in the wrong order")
    print(amount_in_wrong_order[-10:])
    print("the number of packets that was slower than 1 ns")
    print(amount_with_zero[-10:])

    print("Have saved the parsed results, ending the program")


# run main 
if __name__=="__main__":
    main()