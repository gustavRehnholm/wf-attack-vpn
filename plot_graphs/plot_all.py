#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool

from plot_figure import plot_figure

'''
To run:
python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/ -w 10
'''

ap = argparse.ArgumentParser()
ap.add_argument("-r"   , required = True , type = str, default = "wf_result", 
    help="root folder of the DF result")
ap.add_argument("-w"   , required = False, type = int, default = 10, 
    help="number of workers for loading traces from disk")
ap.add_argument("--ylim_lower"   , required = False, type = float, default = 0.5, 
    help="lower y limitation")
ap.add_argument("--ylim_higher"  , required = False, type = float, default = 1, 
    help="higher y limitation")
args = vars(ap.parse_args())

def main():
    '''
    PLot graph for all the provided results.
    The expected structure
    input -> one folder foreach figure -> one folder for each subplot -> one file for each line to plot on the subplot
    '''

    input       = []
    p           = Pool(args['w'])
    result_path = args["r"]
    y_lim = [args["ylim_lower"], args["ylim_higher"]]

    # plot one figure for each folder in the 
    for curr_dir in os.listdir(result_path):
        files2plot = f"{result_path}{curr_dir}"
        sup_title  = curr_dir

        input.append((files2plot, 'Threshold', 'Accuracy',y_lim, sup_title, "fig/twitch/"))

    p.starmap(plot_figure, input)
    
if __name__ == "__main__":
    main()