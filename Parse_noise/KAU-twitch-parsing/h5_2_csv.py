#!/usr/bin/python3

'''
Convert the data in h5 format to csv, to check for any problems in the converting steps
Only necessary to run for bug hunting

python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/h5_2_csv.py
'''

import pandas as pd
import os

def main():
    print("Start generating csv file")

    # the usable captures
    DIR_INPUT = "twitch/merged_captures/"
    # the csv files 
    DIR_OUTPUT = "twitch/captures_csv/"

    key = "df"
    index = 0

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    for file in os.listdir(DIR_INPUT):
        filename = os.fsdecode(file)

        index += 1
        print("")
        print("converting file " + str(index) + "/1370: " + str(filename))
        print("")

        path = DIR_INPUT + filename
        df = pd.read_hdf(path, key=key)

        csv_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.csv'
        df.to_csv(csv_file_name, index = True)


# run main 
if __name__=="__main__":
    main()