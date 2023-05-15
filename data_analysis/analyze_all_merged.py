#!/usr/bin/env python3

import argparse
import os

from merged_analysis import merged_analysis

'''
To run:
python wf-attack-vpn/data_analysis/analyze_all_merged.py -d merged_traffic -w 10 --fold foreground_traffic/fold-0.csv
'''

ap = argparse.ArgumentParser()
ap.add_argument("-d"   , required = True , type = str, default = "", 
    help="root folder of the merged dataset")

ap.add_argument("-r", "--result", required = True , type = str,
    help="root folder of the overhead result")

ap.add_argument("-w"   , required = False, type = int, default = 10, 
    help="number of workers for loading traces from disk")

ap.add_argument("--fold", required = False, type = str, default = "foreground_traffic/fold-0.csv", 
    help="Path to the fold file to use")
    
args = vars(ap.parse_args())

def main():
    '''
    Analyze all merged datasets that are in the provided folder
    '''
    dirs = os.listdir(args["d"])
    for curr_dir in dirs:
        folder = args['d'] + "/" + curr_dir
        os.mkdir(args['result'])
        fname  = f"{args['result']}/{curr_dir}.txt"
        merged_analysis(dir = folder, workers = args['w'], fold = args["fold"], fname = fname)
    
if __name__ == "__main__":
    main()