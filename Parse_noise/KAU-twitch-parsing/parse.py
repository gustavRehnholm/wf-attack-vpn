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

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    curr_file_index = 0

    

    dictionary_parsed = {
        'time': [],
        'direction': [],
        'size': []
    }
    for file in os.listdir(DIR_INPUT):
        # prepare df_parsed for the new file
        # This did porbably not work! 
        #df_parsed = df_parsed.iloc[0:0]

        df_parsed = pd.DataFrame(columns = ['time', 'direction', 'size'])

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


            sender_receiver = str(row['sender_receiver']).split(",")
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
                parsed_size = int(row['size']) - HEADER
            except:
                continue

            if parsed_size <= 0:
                continue

            dictionary_parsed['time'].append(parsed_time)
            dictionary_parsed['direction'].append(parsed_direction)
            dictionary_parsed['size'].append(parsed_size)

        # have parsed the whole file, store the result
        df_parsed = pd.DataFrame(dictionary_parsed)
        df_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.h5'
        df_parsed.to_hdf(df_file_name, mode = "w", key = key) 


# run main 
if __name__=="__main__":
    main()