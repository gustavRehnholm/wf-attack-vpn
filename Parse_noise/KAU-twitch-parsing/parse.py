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
'''

import pandas as pd
import os

def main():
    print("Start generating csv file")

    # the usable captures
    DIR_INPUT = "twitch/usable_captures_h5/"
    # for the parsed captures
    DIR_OUTPUT = "twitch/parsed_captures/"
    # how many nanoseconds in a second
    NANO_SEC_PER_SEC = 1000000
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

    # to inform the user how long the script has run
    curr_file_index = 0
    total_files = len(input_files)
    
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
        print("parsing file " + str(curr_file_index) + "/1362: " + str(filename))
        print("")

        # get the data from the current file
        path = DIR_INPUT + filename
        df   = pd.read_hdf(path, key=key)

        first_row = True

        for row in df.itertuples():

            if first_row:
                prev_time = 0
            first_row = False

            # convert from timestamp in sec, to duration form last packet in ns
            if not row[time_index]:
                continue
            else:
                # get the time for the data (convert from seconds with 9 float numbers, to nanoseconds as a integer)
                left_of_dot, right_of_dot = divmod(row[time_index], 1)
                left_of_dot  = left_of_dot * NANO_SEC_PER_SEC
                right_of_dot = right_of_dot * NANO_SEC_PER_SEC
                totalTimeParseLine  = int(LeftOfDotInNanoSec + RightOfDotInNanoSec)

                parsed_time = totalTimeParseLine - prev_time

                if parsed_time < 0:
                    print("ERROR: the time between two packet was less than 0! duration = " + str(totalTimeParseLine) + " - " + str(prev_time))
                    print(parsed_time)
                    return


            sender_receiver = str(row[sender_receiver_index]).split(",")
            # if no or only one IP address, skip this packet
            if len(sender_receiver) < 2:
                continue
            else:
                sender          = sender_receiver[0]
                receiver        = sender_receiver[1]

                # get direction
                if sender == "":
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
                continue

            if parsed_size <= 0:
                continue

            dictionary_parsed['time'].append(parsed_time)
            dictionary_parsed['direction'].append(parsed_direction)
            dictionary_parsed['size'].append(parsed_size)

            # update time for the packet before (in ns)
            prev_time = totalTimeParseLine

        # have parsed the whole file, store the result
        df_parsed = pd.DataFrame(dictionary_parsed)

        #df_parsed.to_csv("tmp.csv", index = True)
        #return

        df_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.h5'
        df_parsed.to_hdf(df_file_name, mode = "w", key = key) 


# run main 
if __name__=="__main__":
    main()