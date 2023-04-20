#!/usr/bin/python3

'''
Convert the data in h5 format to csv, to check for any problems in the converting steps
Only necessary to run for bug hunting

python wf-attack-vpn/parse_background/h5_2_csv.py background_traffic/twitch_1_first.h5
'''

import pandas as pd
import os
import sys

def main():
    print("Start generating csv file")

    '''
    # the files to create csv files of
    DIR_INPUT = sys.argv[1]
    # the csv files 
    DIR_OUTPUT = "captures_csv/"

    # to extract the dataframe from the h5 file
    key = "df"
    # to inform the user how far the program has traversed
    index = 0

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    #files = os.listdir(DIR_INPUT)
    files = ["background_traffic/twitch_1_first.h5"]
    len_files = len(files)

    # for every h5 file, create a csv file
    for file in files:
        filename = os.fsdecode(file)

        index += 1
        print("")
        print("converting file " + str(index) + "/" + str(len_files) + ": " + str(filename))
        print("")

        #path = DIR_INPUT + filename
        path = file
        df = pd.read_hdf(path, key=key)

        csv_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.csv'
        df.to_csv(csv_file_name, index = True)
    '''
    path = "background_traffic/twitch_1_first.h5"
    df = pd.read_hdf(path, key="df")

    csv_file_name = "captures_csv/twitch_1_first.csv"
    df.to_csv(csv_file_name, index = True)

# run main 
if __name__=="__main__":
    main()