#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool
import numpy as np
import sys

# python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/0/twitch_largest_1

ap = argparse.ArgumentParser()
ap.add_argument("-d", required = True , type = str, default = "", help="root folder of client/server dataset")
ap.add_argument("-w", required = False, type = int, default = 10, help="number of workers for loading traces from disk")
args = vars(ap.parse_args())

def main():
    '''
    Analyze merged datasets, to see how much of the packets are from the foreground and background
    '''

    print(f"walking directory {args['d']}, this might take some time...")
    print("")

    # walk the dataset folder
    todo = []
    dirs = os.listdir(args["d"])

    # for each webpage dir
    for curr_dir in dirs:
        folder = args['d'] + "/" + curr_dir
        # for all log files for each webpage
        for root, dirs, files in os.walk(folder, topdown = False):
            for name in files:
                if ".log" in name:
                    todo.append((os.path.join(root, name), name))


    p = Pool(args["w"])

    # 92 000 inputs
    input = []
    for file in todo:
        input.append( (file, 1) )

    # to test with one packet
    #input = [("foreground_traffic/client/0/0000-0001-0047.log",intervals)]

    file_stats = p.starmap(percent_foreground, input)
    np_stat    = np.array(file_stats)

    try:
        # print some descriptive statistics
        print(stat_txt("Foreground percent" , np_stat))
    except:
        print("ERROR while calculating stastics")
        return
    

def percent_foreground(fname, dir_index):
    '''
    Get the percentage of how much of the files lines comes from the foreground dataset
    '''
    background_packets = 0
    foreground_packets = 0
    with open(fname, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            dir = int(parts[dir_index])
            if dir == "sb" or dir == "rb":
                background_packets += 1
            elif dir == "s" or dir == "r":
                foreground_packets += 1
            else:
                print(f"ERROR: direction {dir} is not valid")
                sys.exit()

    percent_foreground = (foreground_packets)/(background_packets + foreground_packets)
    percent_foreground = percent_foreground * 100
    return percent_foreground


def stat_txt(description_text, np_array):
    '''
    format how to print statistics 
    Input:
        description_text: short string (1-3 words) to describe what the statistics is for 
        np_array        : what to show statistics for 
    Output:
        string to print
    '''
    txt = "{description:>13}: {mean:>15.2f} +- {std:>15.2f}, median: {median:>15.2f},  min: {min:>15.2f}, max: {max:>15.2f}"

    return txt.format(description = description_text   , mean = np.mean(np_array), std = np.std(np_array), 
                      median      = np.median(np_array), min  = np.min(np_array) , max = np.max(np_array))

if __name__ == "__main__":
    main()