#!/usr/bin/env python3

import pandas as pd
import numpy as np

df = pd.read_hdf("VNAT_Dataframe_release_1.h5")
print("Number of rows: ", len(df))


num_vpn = 0
num_nonvpn = 0

keywords = ["youtube", "netflix", "vimeo", "voip", "skype-chat", "ssh", "rdp", "sftp", "rsync", "scp"]
total_time = {}
total_packets = {}

for index, row in df.iterrows():
    fname = row["file_names"]

    if fname.startswith("nonvpn"):
        num_nonvpn += 1
        continue
    
    num_vpn += 1
        
    # get total time
    t = np.array(row["timestamps"])
    delta = np.max(t) - np.min(t)
    total_time["total"] = total_time.get("total", 0) + delta

    # if keyword in fname, add to that keyword in total_time
    for keyword in keywords:
        if keyword in fname:
            total_time[keyword] = total_time.get(keyword, 0) + delta
            break
    
    # get total packets
    packets = np.array(row["directions"])
    total_packets["total"] = total_packets.get("total", 0) + len(packets)

    # if keyword in fname, add to that keyword in total_packets
    for keyword in keywords:
        if keyword in fname:
            total_packets[keyword] = total_packets.get(keyword, 0) + len(packets)
            break

print("number of non-VPN rows: ", num_nonvpn)
print("number of VPN rows: ", num_vpn)

print("")
for k, v in total_time.items():
    # format with 2 decimal places
    print(f"{k:10} {v / 3600:6.2f} hours, {total_packets[k] / (1000*1000):6.2f} million packets, {total_packets[k] / v:8.2f} packets/s")