#!/usr/bin/python3

'''
To run
python wf-attack-vpn/data_analysis/rds_collect_analysis.py
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
    Analyze the provided raw captures from rds-collect

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
    # stat for one file
    f = open("file_0",'w')
    file_0   = time_lists[0][0]
    print(file_0, file = f)

    f = open("file_40",'w')
    file_40  = time_lists[40][0]
    print(file_40, file = f)

    f = open("file_60",'w')
    file_60  = time_lists[60][0]
    print(file_60, file = f)

    f = open("file_80",'w')
    file_80  = time_lists[80][0]
    print(file_80, file = f)

    # smallest
    f = open("file_-1",'w')
    file__1  = time_lists[-1][0]
    print(file__1, file = f)

    f = open("file_-100",'w')
    file__100  = time_lists[-100][0]
    print(file__100, file = f)

    f = open("file_-200",'w')
    file__200  = time_lists[-200][0]
    print(file__200, file = f)

    f = open("file_-300",'w')
    file__300  = time_lists[-300][0]
    print(file__300, file = f)

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
        upper_limit_h.append(dic['upper_limit_h'])

    upper_limit_h.sort()
    print(f"Shortest and longest duration of the captures: [{upper_limit_h[0]:.2f},{upper_limit_h[-1]:.2f}]")


    # plot a line for min, max and mean
    plot_analysis(min = min, max = max, mean = mean)
    # plot stats for individual capture files
    plot_analysis_captures(cap1 = file_0, cap2 = file_40, cap3 = file_60, cap4 = file_80)
    # plot stats for individual capture files
    plot_analysis_captures(cap1 = file__1, cap2 = file__100, cap3 = file__200, cap4 = file__300, subtitle= ['-1', '-100', '-200', '-300'], title = "twitch_smallest_captures")

    return


def timestamps_capture(path_file2analyze, index):
    '''
    get list of number of packet, each second, for the file

    Args:
        path_file2analyze - Required : path to the file  (str)
        index             - Required : index of the file (int)
    Return:
        Tuple consisting of 3 elements

        time_list : 
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
    '''
    Get min, max, mean for the provided timestamp list
    Args:
        timestamp_list - Required : list of pkt/sec for each sec interval     (List[int])
        index          - Required : index of the file (so it do not get lost) (int)
        upper_limit    - Required : converts it from s to h                   (float)
    '''
    np_timestamp = np.array(timestamp_list)

    min  = np.min(np_timestamp)
    max  = np.max(np_timestamp)
    mean = np.mean(np_timestamp)

    upper_limit_h = upper_limit/(60*60)

    return {"stat": (min, max, mean),
            "index": index,
            "upper_limit_h" : upper_limit_h}


def plot_analysis_captures(cap1, cap2, cap3, cap4, subtitle = ['0', '40', '60', '80'], title = "Twitch_singular_captures", result_path = "fig/"):
    '''
    Plot a graph to show how the captured data from rds-collect behavior
    Args:
        cap1-4      - Required : Behavior of one file                  (List[int])
        title       - Optional : title of the figure                   (str)
        result_path - Optional : Where to store the figure             (str)

    '''

    plt.subplot(2, 2, 1)
    plt.plot(cap1)
    plt.title(f'file:{subtitle[0]}')
    plt.ylabel('pkt/s')
    plt.xlabel('time(sec)')

    plt.subplot(2, 2, 2)
    plt.plot(cap2)
    plt.title(f'file:{subtitle[1]}')
    plt.ylabel('pkt/s')
    plt.xlabel('time(sec)')

    plt.subplot(2, 2, 3)
    plt.plot(cap3)
    plt.title(f'file:{subtitle[2]}')
    plt.ylabel('pkt/s')
    plt.xlabel('time(sec)')

    plt.subplot(2, 2, 4)
    plt.plot(cap4)
    plt.title(f'file:{subtitle[3]}')
    plt.ylabel('pkt/s')
    plt.xlabel('time(sec)')

     # save result and clear the plotting
    plt.tight_layout()
    plt.suptitle(title)
    plt.savefig(f"{result_path}{title}.png")
    plt.close()

    return

def plot_analysis(min, max, mean, title = "Twitch_combined_captures", result_path = "fig/"):
    '''
    Plot a graph to show how the captured data from rds-collect behavior
    Args:
        min         - Required : list of lowest pkt/sec for each file  (List[int])
        max         - Required : list of highest pkt/sec for each file (List[int])
        mean        - Required : list of mean pkt/sec for each file    (List[int])
        one_file    - Required : Behavior of one file                  (List[int])
        title       - Optional : title of the figure                   (str)
        result_path - Optional : Where to store the figure             (str)

    '''

    fig, axes = plt.subplots(2, 2, figsize=(10, 5))
    fig.subplots_adjust(top=0.8)

    axes[0,0].plot(mean)
    axes[0,0].set_title('mean')
    axes[0,0].ylabel('pkt/s')
    axes[0,0].xlabel('file')

    axes[1,0].plot(max)
    axes[0,0].set_title('max')
    axes[0,0].ylabel('pkt/s')
    axes[0,0].xlabel('file')

    axes[1,1].plot(min)
    axes[0,0].set_title('min')
    axes[0,0].ylabel('pkt/s')
    axes[0,0].xlabel('file')

    # save result and clear the plotting
    fig.tight_layout()
    fig.suptitle(title)
    fig.savefig(f"{result_path}{title}.png")
    fig.close()

    return

if __name__=="__main__":
    main()