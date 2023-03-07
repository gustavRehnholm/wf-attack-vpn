#!/usr/bin/python3

'''
Parse the twitch noise, which is converted to dataframes in the h5 format

# name for the attributes
COL_NAMES =  ['time', 'sender_receiver', 'size']

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

    curr_file_index = 0

    df_parsed = pd.DataFrame(columns = ['time', 'direction', 'size'])

    for file in os.listdir(DIR_INPUT):
        df_parsed = df_parsed.iloc[0:0]
        curr_file_index += 1
        filename = os.fsdecode(file)
        
        print("")
        print("parsing file " + str(curr_file_index) + "/1362: " + str(filename))
        print("")

        path = DIR_INPUT + filename
        df = pd.read_hdf(path, key=key)

        for index, row in df.iterrows():
            # convert from sec to ns
            if not row['time']:
                continue
            else:
                time = float(row['time']) * NANO_SEC_PER_SEC
                parsed_time = int(time)

            sender_receiver = row['sender_receiver'].split(",")
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
                parsed_size = int(row['size']) - HEADER
            except:
                continue

            if parsed_size <= 0:
                continue

            # add the parsed packet to the new dataframe
            new_packet = {
                'time': [parsed_time], 
                'direction': [parsed_direction], 
                'size': [parsed_size]
            }

            new_df = pd.DataFrame(new_packet)
            pd.concat(df_parsed, new_df)

        # have parsed the whole file, store the result
        df_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.h5'
        df_parsed.to_hdf(df_file_name, mode = "w", key = key) 


# run main 
if __name__=="__main__":
    main()