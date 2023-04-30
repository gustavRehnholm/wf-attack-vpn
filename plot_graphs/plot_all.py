#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool

from plot_figure import plot_figure

'''
To run:
python wf-attack-vpn/plot_graphs/plot_all.py -d merged_traffic -w 10
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

    input = []
    p = Pool(args['w'])

    # plot one figure for each folder in the 
    for curr_dir in os.listdir(args["d"]):
        files2plot = []
        sub_title  = []
        sup_title  = curr_dir
        path = args['d'] + "/" + curr_dir
        for curr_file in os.listdir(path):
            files2plot.append(f"{path}/{curr_file}")
            sub_title.append(curr_file)

        input.append((files2plot, sub_title, 'Threshold', 'Accuracy', sup_title))

    p.starmap(plot_figure, input)
    
if __name__ == "__main__":
    main()