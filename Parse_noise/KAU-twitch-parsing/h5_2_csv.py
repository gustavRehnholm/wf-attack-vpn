#!/usr/bin/python3

'''
Convert the data in h5 format to csv, to check for any problems in the converting steps

python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/h5_2_csv.py
'''

import pandas as pd
import os

def main():
    print("Start generating csv file")

    # the usable captures
    DIR_RAW_USABLE_NOISE = "twitch/usable_captures_h5/"
    # the csv files 
    DIR_CSV = "twitch/usable_captures_csv/"

    key = "df"

    index = 0
    for file in os.listdir(DIR_RAW_USABLE_NOISE):
        filename = os.fsdecode(file)

        index += 1
        print("")
        print("converting file " + str(index) + "/1362: " + str(filename))
        print("")

        path = DIR_RAW_USABLE_NOISE + filename
        df = pd.read_hdf(path, key=key)

        csv_file_name = DIR_CSV + filename.rsplit('.', 1)[0] + '.csv'
        df.to_csv(csv_file_name, index = True)


# run main 
if __name__=="__main__":
    main()