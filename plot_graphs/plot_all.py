#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool

from plot_figure import plot_figure

'''
To run:
python wf-attack-vpn/plot_graphs/plot_all.py -d merged_traffic -w 10 --fold foreground_traffic/fold-0.csv
'''

ap = argparse.ArgumentParser()
ap.add_argument("-d"   , required = True , type = str, default = "wf_result/", 
    help="root folder of the merged dataset")
ap.add_argument("-w"   , required = False, type = int, default = 10, 
    help="number of workers for loading traces from disk")
args = vars(ap.parse_args())

def main():
    '''
    PLot graph for all the provided results.
    The expected structure
    input -> one folder foreach figure -> one folder for each subplot -> one file for each line to plot on the subplot
    '''

    dirs = os.listdir(args["d"])
    for curr_dir in dirs:
        subplot_folder = args['d'] + "/" + curr_dir
        print(curr_dir)

        #fname  = f"{curr_dir}.png"
        #plot_figure(dir = subplot_folder, workers = args['w'], fold = args["fold"], fname = fname)
    
if __name__ == "__main__":
    main()