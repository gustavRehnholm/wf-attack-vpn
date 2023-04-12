#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool
import numpy as np
import sys
from collections import Counter

# python wf-attack-vpn/merged-dataset-stats.py -d captures

ap = argparse.ArgumentParser()
ap.add_argument("-d", required=True, default="", help="root folder of client/server dataset")
ap.add_argument("-w", required=False, type=int, default=10,
    help="number of workers for loading traces from disk")
ap.add_argument("--min", required=False, type=int, default=0, help="smallest packet size to consider")
args = vars(ap.parse_args())


def main():
    '''
    Analyse all capture files in a directory, generated by rds-collect
    '''

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

    # store statistics gathered from the file
    sent_lines, recv_lines = [], []
    sent_bytes, recv_bytes = [], []
    pkt_sec, total_time    = [], []
    size                   = []
    multiple_clients_nr    = []
    multiple_clients_file  = []
    one_client             = []

    for result in results:
        if result.get("success") == True:
            # only analyse files that have one client
            if result.get("clients") == 1:
                sent_lines.append(result.get("sent_lines"))
                recv_lines.append(result.get("recv_lines"))
                sent_bytes.append(result.get("sent_bytes"))
                recv_bytes.append(result.get("recv_bytes"))
                one_client.append(result.get("fname"))
                pkt_sec.append(result.get("pkt_sec"))
                size.append(result.get("size"))
                total_time.append(result.get("total_time"))
            else:
                multiple_clients_nr.append(result.get("clients"))
                multiple_clients_file.append(result.get("fname"))

    # convert to numpy arrays
    sent_lines = np.array(sent_lines)
    recv_lines = np.array(recv_lines)
    sent_bytes = np.array(sent_bytes)
    recv_bytes = np.array(recv_bytes)
    pkt_sec    = np.array(pkt_sec)
    total_time = np.array(total_time)
    size       = np.array(size)

    try:
        txt = "{description}: {mean:.2f} +- {std:.2f}, median: {median:.2f},  min: {min}, max: {max}"
        # print some descriptive statistics
        print(txt.format(description = "sent lines"         , mean = np.mean(sent_lines), std = np.std(sent_lines), 
                         median      = np.median(sent_lines), min  = np.min(sent_lines) , max = np.max(sent_lines)))
        print(f"recv lines: {np.mean(recv_lines):.2f} +- {np.std(recv_lines):.2f}, median: {np.median(recv_lines):.2f},  min: {np.min(recv_lines)}, max: {np.max(recv_lines)}")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"sent bytes: {np.mean(sent_bytes):.2f} +- {np.std(sent_bytes):.2f}, median: {np.median(sent_bytes):.2f}, min: {np.min(sent_bytes)}, max: {np.max(sent_bytes)}")
        print(f"recv bytes: {np.mean(recv_bytes):.2f} +- {np.std(recv_bytes):.2f}, median: {np.median(recv_bytes):.2f}, min: {np.min(recv_bytes)}, max: {np.max(recv_bytes)}")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"packets/sec: {np.mean(pkt_sec):.2f} +- {np.std(pkt_sec):.2f}, median: {np.median(pkt_sec):.2f}, min: {np.min(pkt_sec)}, max: {np.max(pkt_sec)}")
        print(f"duration   : {np.mean(total_time):.2f} +- {np.std(total_time):.2f}, median: {np.median(total_time):.2f}, min: {np.min(total_time)}, max: {np.max(total_time)}")
        print(f"size       : {np.mean(size):.2f} +- {np.std(size):.2f}, median: {np.median(size):.2f}, min: {np.min(size)}, max: {np.max(size)}")
        '''
        print(f"sent lines: {np.mean(sent_lines):.2f} +- {np.std(sent_lines):.2f}, median: {np.median(sent_lines):.2f},  min: {np.min(sent_lines)}, max: {np.max(sent_lines)}")
        print(f"recv lines: {np.mean(recv_lines):.2f} +- {np.std(recv_lines):.2f}, median: {np.median(recv_lines):.2f},  min: {np.min(recv_lines)}, max: {np.max(recv_lines)}")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"sent bytes: {np.mean(sent_bytes):.2f} +- {np.std(sent_bytes):.2f}, median: {np.median(sent_bytes):.2f}, min: {np.min(sent_bytes)}, max: {np.max(sent_bytes)}")
        print(f"recv bytes: {np.mean(recv_bytes):.2f} +- {np.std(recv_bytes):.2f}, median: {np.median(recv_bytes):.2f}, min: {np.min(recv_bytes)}, max: {np.max(recv_bytes)}")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f"packets/sec: {np.mean(pkt_sec):.2f} +- {np.std(pkt_sec):.2f}, median: {np.median(pkt_sec):.2f}, min: {np.min(pkt_sec)}, max: {np.max(pkt_sec)}")
        '''
    except:
        print("ERROR while calculating stastics")
    print(f" {len(one_client)} files are with 1 client")
    if len(multiple_clients_nr) > 0:
        print(f" {len(multiple_clients_nr)} files are with to many clients, with the distribution: ")
        print(Counter(multiple_clients_nr))
        for file in multiple_clients_file:
            print(file)


def parse_trace(fname, name):
    '''
    Get statistics from a capture file, generated by rds-collect
    Input:
        fname: path and name to the file which should be analyzed
        name: 
    Output:
        Tuple with statistics of the file
        Boolean               :  If it succeeded in gathering the files statistics
        sent_lines, recv_lines:  The number of packets that was sent/received
        sent_bytes, recv_bytes:  The sent/received packets total size in bytes
        clients               :  Number of clients used in the stream
        pkt_sec               :  Packets per second in the stream
        fname                 :  The file that was analyzed
    '''

    # gathered statistics
    sent_lines, recv_lines = 0, 0
    sent_bytes, recv_bytes = 0, 0
    clients = 0

    ipHost = 'temporary placeholder name'
    
    with open(fname, "r") as f:
        for line in f:

            # parts: ["time", "sender,reciever", "size"]
            parts = line.strip().split("\t")

            # unusable lines that would not be used either way
            if len(parts) < 3:
                continue

            direction = parts[1]
            size      = int(parts[2])

            if size < args["min"]:
                continue

            # sender_receiver: [sender, receiver]
            sender_receiver = str(direction).split(",")

            # if no or only one IP address, skip this packet
            if len(sender_receiver) < 2:
                continue
            else:
                sender          = sender_receiver[0]
                receiver        = sender_receiver[1]

                # get direction
                if sender == "":
                    continue
                elif receiver == "":
                    continue 
                elif sender == ipHost:
                    sent_bytes += size
                    sent_lines += 1
                elif receiver == ipHost:
                    recv_bytes += size
                    recv_lines += 1
                else:
                    if sender.split('.')[0] == '10':
                        clients += 1
                        ipHost = sender
                        sent_bytes += size
                        sent_lines += 1
                    elif receiver.split('.')[0] == '10':
                        clients += 1
                        ipHost = receiver
                        recv_bytes += size
                        recv_lines += 1
                    else:
                        continue
    total_time = float(parts[0])
    pkt_sec = (sent_lines + recv_lines) / total_time
    size = os.path.getsize(fname)
    return dict(success = True, 
                sent_lines = sent_lines, 
                recv_lines = recv_lines, 
                sent_bytes = sent_bytes, 
                recv_bytes = recv_bytes, 
                clients = clients, 
                pkt_sec = pkt_sec, 
                total_time = total_time,
                size = size,
                fname = fname)



if __name__ == "__main__":
    main()
