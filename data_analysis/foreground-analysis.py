#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool
import numpy as np
import pandas as pd
import sys
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

# python wf-attack-vpn/data_analysis/foreground-analysis.py -d foreground_traffic/client


ap = argparse.ArgumentParser()
ap.add_argument("-d", required=True, default="", help="root folder of client/server dataset")
ap.add_argument("-w", required=False, type=int, default=10,
    help="number of workers for loading traces from disk")
ap.add_argument("--min", required=False, type=int, default=0, help="smallest packet size to consider")
args = vars(ap.parse_args())


def main():
    '''
    Analyze all capture files in a directory, generated by rds-collect
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

    intervals = 20

    # 92 000 inputs
    input = []
    for file in todo:
        input.append( (file[0], intervals) )

    # to test with one packet
    #input = [("foreground_traffic/client/0/0000-0001-0047.log",intervals)]

    list_of_traces = p.starmap(parse_trace, input)
    pkt_sec = get_pkt_sec(list_of_traces, intervals)
    print(pkt_sec)

    print("Saved the result")


def parse_trace(fname, interval):
    '''
    get packet timestamp, of all packets the first 15 seconds, generated by Tobias Pulls
    Input:
        fname: path and name to the file which should be analyzed
        interval: how many intervals (of seconds) to analyze
    Output:
        List of timestamps (in ns) of the packets
    '''
    ns          = 1000000000
    upper_limit = ns * interval
    with open(fname, "r") as f:
        timestamp = []
        for line in f:
            # parts: ["time(ns)", "direction", "size"]
            parts = line.strip().split(",")
            time = int(parts[0])
            if (time < upper_limit):
                timestamp.append(time)
            else:
                break

    return timestamp


def get_pkt_sec(list_of_traces, interval):
    '''
    returns list of mean number of packets per second interval
    '''

    ns           = 1000000000
    intervals    = interval
    upper        = [0] * intervals
    lower        = [0] * intervals
    pkt_interval = [0] * intervals
    pkt_sec      = [0] * intervals
    labels       = [""] * intervals 
    len_traces   = len(list_of_traces)

    print(f"Number of log files: {len_traces}")

    for i in range(0,intervals):
        lower[i] = ns * i
        upper[i] = ns * (i + 1)

    # for every packet, in every trace, get which interval it belongs to
    for trace in list_of_traces:
        for packet in trace:
            # determine which interval the packet belongs to
            added_pkt = False
            i = 0
            while(not added_pkt):
                if packet >= lower[i] and packet < upper[i]:
                    pkt_interval[i] += 1
                    added_pkt = True

                i += 1
                if (not added_pkt) and (i >= intervals):
                    print("ERROR: packet could not be found in a interval")
                    print(packet)
                    sys.exit()

    # get mean value of number of packets, during each second interval
    for j in range(len(pkt_interval)):
        pkt_sec[j] = pkt_interval[j] / len_traces

    # description of each interval
    for k in range(len(pkt_sec)):
        labels[k] = ("[" + str(k) + "," + str(k+1) + "[")

    d = {"pkt/sec" : pkt_sec, "pkt" : pkt_interval, "interval (sec)" : labels}
    df = pd.DataFrame(d)
    return df

if __name__ == "__main__":
    main()
