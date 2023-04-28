#!/usr/bin/python3

'''
To run
python wf-attack-vpn/parse_background/KAU-twitch-parsing/analyze_dataset.py --input twitch/tmp/ --workers 10
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
ap.add_argument("--input"  , required = False, default = "twitch/parsed_captures/"  , type = str, help = "Directory for the files to analyze")
ap.add_argument("--output" , required = False, default = "fig/twitch_analysis/"     , type = str, help = "Directory to store the result")
ap.add_argument("--workers", required = False, default = 10                         , type = int, help = "Workers for multiprocessing")
args = vars(ap.parse_args())


def main():
    '''
    Analyze the provided background traffic
    '''
    print("Start analyzing background")
    analyze_dataset(dir_input   = args['input'],
                    dir_output  = args['output'],
                    workers     = args['workers'])
    return


def analyze_dataset(dir_input = "twitch/parsed_captures/", dir_output = "fig/twitch_analysis", workers = 10):
    '''
    Analyze the parsed Twitch dataset

    Args:
        dir_input  - Optional : Path to the captures to analyze (str)
        dir_output - Optional : Path to the twitch analysis     (str)
        workers    - Optional : Workers for multiprocessing     (int)
    '''

    # usable captures, sorted after size (descending)
    input_files = os.listdir(dir_input)
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
    sorted_stats = sorted(stat_lists, key = lambda d: d['index'])
    min  = []
    max  = []
    mean = []
    for dic in sorted_stats:
        min.append(dic['stat'][0])
        max.append(dic['stat'][1])
        mean.append(dic['stat'][2])
    # plot a line for min, max and mean
    plot_analysis(min, max, mean, "Twitch_analysis", "fig/")

    return


def timestamps_capture(path_file2analyze, index):
    '''
    get list of number of packet, each second, for the file

    Args:
        path_file2analyze - Required : path to the file                       (str)
    '''
    NS_PER_SEC       = 1000000000
    TUPLE_TIME_INDEX = 0

    # the background packets as a list of tuples (better performance than working with the dataframe)
    df               = pd.read_hdf(path_file2analyze, key = "df")
    background_tuple = list(df.itertuples(index=False, name=None))
    background_len   = len(background_tuple)
    # the result
    time_list        = [0] * background_len
    # keep track of current packet and time interval
    interval_index   = 0
    tuple_index      = 0
    # which timestamp the packet is sent in
    curr_timestamp   = int(background_tuple[tuple_index][TUPLE_TIME_INDEX])
    
    while tuple_index < background_len-1:
        # advance the time with the duration of the next packet
        lower_limit = interval_index     * NS_PER_SEC
        upper_limit = (interval_index+1) * NS_PER_SEC
        #print(f"current time: {curr_timestamp}, interval: [{lower_limit},{upper_limit}]")
        # this packet is in the current interval
        if curr_timestamp >= lower_limit and curr_timestamp < upper_limit:
            time_list[interval_index] += 1
            tuple_index               += 1
            curr_timestamp += int(background_tuple[tuple_index][TUPLE_TIME_INDEX])
        # advance the interval
        elif curr_timestamp >= upper_limit:
            interval_index += 1
        # the packet is probably in the wrong order
        else:
            print(f"ERROR: the time {curr_timestamp} should not be able to go below the current lower interval {lower_limit}")
            print(f"Upper limit: {upper_limit}")
            sys.exit()

    return (time_list, index)


def stat(timestamp_list, index):
    np_timestamp = np.array(timestamp_list)

    min  = np.min(np_timestamp)
    max  = np.max(np_timestamp)
    mean = np.mean(np_timestamp)

    return {"stat": (min, max, mean),
            "index": index}


def plot_analysis(min, max, mean, title = "untitled", result_path = "fig/"):
    '''

    '''

    plt.plot(mean)
    plt.plot(max)
    plt.plot(min)

    plt.ylabel('pkt/s')
    plt.xlabel('file')

    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom = 0.15)

    plt.legend()
    plt.title(title)
    #fig = plt.gcf()
    file_path = result_path + title + ".png"
    f = open(file_path, "w")
    f.close()
    plt.savefig(file_path)

    #plt.show()

    return

if __name__=="__main__":
    main()