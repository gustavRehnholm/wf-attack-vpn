#!/usr/bin/python3

'''
Parse the twitch noise, which is converted to dataframes in the h5 format

# name for the attributes
COL_NAMES =  ['time', 'sender', 'receiver', 'size']

touch stdout/parse.py
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/parse.py | tee stdout/parse.py
'''

import pandas as pd
import os

def main():
    print("Start generating csv file")

    # the usable captures
    DIR_RAW_USABLE_NOISE = "twitch/usable_captures_h5/"
    # for the parsed captures
    DIR_PARSED_NOISE = "twitch/parsed_captures/"
    # how many nanoseconds in a second
    NANO_SEC_PER_SEC = 1000000
    # How much of the header to remove (to fit the noise with the web traffic)
    HEADER = 40

    # is used to get the direction of each packet
    ipHost = '10.88.0.9'
    # for storing the result as h5
    key = "df"

    index = 0

    df_parsed = pd.DataFrame(columns = ['time', 'direction', 'size'])

    for file in os.listdir(DIR_RAW_USABLE_NOISE):
        index += 1
        filename = os.fsdecode(file)
        
        print("")
        print("parsing file " + str(index) + "/1370: " + str(filename))
        print("")

        for row in df.rows:
            # convert from sec to ns
            if not row['time']:
                continue
            else:
                parsed_time = int(float(row['time']) * NANO_SEC_PER_SEC)

            # get direction
            if row['sender'] == "":
                continue
            elif row['sender'] == ipHost:
                parsed_direction = "s"
            elif row['receiver'] == ipHost:
                parsed_direction = "r"
            else:
                sender_start_ip = row['sender'].split('.')
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
            new_packet = {'time':parsed_time, 'direction': parsed_direction, 'size': parsed_size}
            new_df = pd.Dataframe(new_packet)
            pd.concat(df_parsed, new_df)

        df_file_name = DIR_PARSED_NOISE + filename.rsplit('.', 1)[0] + '.h5'
        df.to_hdf(df_file_name, mode = "w", key = "df") 


# run main 
if __name__=="__main__":
    main()