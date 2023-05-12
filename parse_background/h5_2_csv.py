#!/usr/bin/python3

'''
Example how to run
python wf-attack-vpn/parse_background/h5_2_csv.py --input mit/raw_app/netflix.h5 --output tmp/netflix.csv
'''

import pandas as pd
import os
import sys
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input"     , required = True, default = "" , type = str, 
    help = "path to the h5 file to convert")
ap.add_argument("--output"     , required = True, default = "" , type = str, 
    help = "path to the csv file to store to")
args = vars(ap.parse_args())

def main():
    '''
    Convert the data in h5 format to csv, to check for any problems in the converting steps
    Only necessary to run for bug hunting
    '''
    path = args["input"]
    df = pd.read_hdf(path, key="df")

    csv_file_name = args["output"]
    df.to_csv(csv_file_name, index = True)

# run main 
if __name__=="__main__":
    main()