#!/usr/bin/env python3

from get_median_acc_10fold import get_median_acc_10fold
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f"     , required = True , default = ""   , type = str, 
    help = "root folder of the merged data to analyse")
args = vars(ap.parse_args())


def main():
    '''
    to run: 
    wf-attack-vpn/data_analysis/median_acc/all_median.py
    args["f"]/dir/mode/fold.csv
    '''

    merged_datasets = os.listdir(args["f"])
    print("---------------------------------")
    for dataset in merged_datasets:
        result = get_median_acc_10fold(dataset)
        print(f"dataset: {dataset}")
        print(f"default: {result[0]}")
        print(f"constant: {result[1]}")
        print(f"tiktok: {result[2]}")
        print("---------------------------------")

if __name__ == "__main__":
    main()