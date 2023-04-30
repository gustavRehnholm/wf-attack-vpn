#!/usr/bin/python3

'''
To run
python wf-attack-vpn/data_analysis/rds_collect_analysis.py

./wf-attack-vpn/data_analysis/rds_collect_analysis.py
'''

from multiprocessing import Pool
import pandas            as pd
import seaborn           as sns
import numpy             as np
import matplotlib.pyplot as plt
import os
import sys
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("--input"  , required = False, default = "captures_clean/"          , type = str, help = "Directory for the files to analyze")
ap.add_argument("--output" , required = False, default = "fig/twitch_analysis/"     , type = str, help = "Directory to store the result")
ap.add_argument("--workers", required = False, default = 10                         , type = int, help = "Workers for multiprocessing")
args = vars(ap.parse_args())


def main():
    '''
    Analyze the provided raw captures from rds-collect
    '''
    print("Start analyzing background")
    background_graph(dir_input   = args['input'],
                    dir_output  = args['output'],
                    workers     = args['workers'])
    return


def background_graph(dir_input = "captures_clean/", dir_output = "fig/twitch_analysis", workers = 10):
    '''
    Analyze the parsed Twitch dataset

    Args:
        dir_input  - Optional : Path to the captures to analyze (str)
        dir_output - Optional : Path to the twitch analysis     (str)
        workers    - Optional : Workers for multiprocessing     (int)
    '''

    # usable captures, sorted after size (descending)
    input_files  = os.listdir(dir_input)
    sorted_files = sorted(input_files, key =  lambda x: os.stat(os.path.join(dir_input, x)).st_size)
    sorted_files = list(reversed(sorted_files))

    input = []
    index = 0
    for curr_file in sorted_files:
        path = dir_input + "/" + os.fsdecode(curr_file)
        input.append((path, index))
        index += 1

    p = Pool(workers)

    # list of pkt/s for each second interval
    print("Start extracting pkt/sec for each sec interval")
    time_lists = p.starmap(timestamps_capture, input)

    # list of min, max and mean pkt/s for each captures
    print("Start extracting min, max and mean for each capture file")
    stat_lists = p.starmap(stat, time_lists)

    print("Plot the data")
    # sort the captures after the original order (size descending)
    sorted_stats = sorted(stat_lists     , key = lambda d: d['index'])

    min  = []
    max  = []
    mean = []
    upper_limit_h = []
    prev_index = -1
    for dic in sorted_stats:
        if prev_index < dic['index']:
            prev_index = dic['index']
        else:
            print(f"ERROR, packets out of order!")
            sys.exit()
        min.append(dic['stat'][0])
        max.append(dic['stat'][1])
        mean.append(dic['stat'][2])
        print(dic['stat'])
        upper_limit_h.append(dic['upper_limit_h'])

    upper_limit_h.sort()
    print(f"time difference [{upper_limit_h[0]:.2f},{upper_limit_h[-1]:.2f}]")

    # plot a line for min, max and mean
    plot_analysis(min, max, mean, "Twitch_analysis", "fig/")


    return


def timestamps_capture(path_file2analyze, index):
    '''
    get list of number of packet, each second, for the file

    Args:
        path_file2analyze - Required : path to the file                       (str)
    '''
    time_list = [0]
    # keep track of current packet and time interval
    interval_index   = 0
    lower_limit = interval_index 
    upper_limit = interval_index + 1

    with open(path_file2analyze, 'r') as file2analyze:
        for file_line in file2analyze: #Reading line by line from the master file since it might be to large to do readlines() on
            split_line = file_line.split("\t")
            time_stamp = float(split_line[0])
            added_line = False
            while added_line == False:
                # advance the interval
                if time_stamp >= upper_limit:
                    interval_index += 1
                    time_list.append(0)
                    # advance the time with the duration of the next packet
                    lower_limit = interval_index
                    upper_limit = interval_index + 1
                # this packet is in the current interval
                else:
                    time_list[interval_index] += 1
                    added_line                 = True


    return (time_list, index, upper_limit)



def stat(timestamp_list, index, upper_limit):
    np_timestamp = np.array(timestamp_list)

    min  = np.min(np_timestamp)
    max  = np.max(np_timestamp)
    mean = np.mean(np_timestamp)

    upper_limit_h = upper_limit

    return {"stat": (min, max, mean),
            "index": index,
            "upper_limit_h" : upper_limit_h}


def plot_analysis(min, max, mean, title = "Twitch_captures", result_path = "fig/"):
    '''

    '''
    plt.subplot(2, 2, 1)
    plt.plot(mean)
    plt.title('mean')

    plt.subplot(2, 2, 2)
    plt.plot(max)
    plt.title('max')

    plt.subplot(2, 2, 3)
    plt.plot(min)
    plt.title('min')

    plt.ylabel('pkt/s')
    plt.xlabel('file')

    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom = 0.15)

    plt.legend()
    suptitle(title)
    #fig = plt.gcf()

    #file_path = f"{result_path}{title}.png"
    # clear old result
    #f = open(file_path, "w")
    #f.close()
    # save new result
    #  , bbox_inches='tight'
    plt.savefig(f"{result_path}{title}.png")

    #plt.show()

    return

if __name__=="__main__":
    main()