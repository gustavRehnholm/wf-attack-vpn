#!/usr/bin/env python3
import argparse
import os
from multiprocessing import Pool
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-d", required=True, default="", help="root folder of client/server dataset")
ap.add_argument("-w", required=False, type=int, default=10,
    help="number of workers for loading traces from disk")
ap.add_argument("--min", required=False, type=int, default=0, help="smallest packet size to consider")
args = vars(ap.parse_args())

def main():
    print(f"walking {args['d']}, this might take a long time...")

    # walk the dataset folder
    todo = []
    for root, dirs, files in os.walk(args["d"], topdown = False):
        for name in files:
            if ".log" in name:
                todo.append(
                    (os.path.join(root, name), name)
                )

    p = Pool(args["w"])
    results = p.starmap(parse_trace, todo)

    sent_lines, recv_lines = [], []
    sent_bytes, recv_bytes = [], []
    for result in results:
        sent_lines.append(result[0])
        recv_lines.append(result[1])
        sent_bytes.append(result[2])
        recv_bytes.append(result[3])

    # convert to numpy arrays
    sent_lines = np.array(sent_lines)
    recv_lines = np.array(recv_lines)
    sent_bytes = np.array(sent_bytes)
    recv_bytes = np.array(recv_bytes)

    # print some descriptive statistics
    print(f"sent lines: {np.mean(sent_lines):.2f} +- {np.std(sent_lines):.2f}, median: {np.median(sent_lines):.2f},  min: {np.min(sent_lines)}, max: {np.max(sent_lines)}")
    print(f"recv lines: {np.mean(recv_lines):.2f} +- {np.std(recv_lines):.2f}, median: {np.median(recv_lines):.2f},  min: {np.min(recv_lines)}, max: {np.max(recv_lines)}")
    #print(f"sent bytes: {np.mean(sent_bytes):.2f} +- {np.std(sent_bytes):.2f}, min: {np.min(sent_bytes)}, max: {np.max(sent_bytes)}")
    #print(f"recv bytes: {np.mean(recv_bytes):.2f} +- {np.std(recv_bytes):.2f}, min: {np.min(recv_bytes)}, max: {np.max(recv_bytes)}")

def parse_trace(fname, name):
    sent_lines, recv_lines = 0, 0
    sent_bytes, recv_bytes = 0, 0
    
    with open(fname, "r") as f:
        n = 0
        for line in f:
            parts = line.strip().split(",")
            direction = parts[1]
            size = int(parts[2])

            if size < args["min"]:
                continue

            if "s" in direction:
                sent_bytes += size
                sent_lines += 1
            elif "r" in direction:
                recv_bytes += size
                recv_lines += 1

    return (sent_lines, recv_lines, sent_bytes, recv_bytes)

if __name__ == "__main__":
    main()
