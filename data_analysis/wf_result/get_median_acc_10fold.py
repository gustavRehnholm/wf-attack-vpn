#!/usr/bin/env python3

import os
import statistics


def get_median_acc_10fold(dir):
    '''
    dir/mode/fold.csv
    Input:
        dir - Required : Which dataset to get the median accuracy
    '''

    modes = ["default", "constant", "tiktok"]
    mode_paths = os.listdir(dir)

    median_default  = []
    median_constant = []
    median_tiktok   = []

    for mode in modes:
        acc_list = []
        for i in range(10):
            csv_path = f"{dir}/{mode}/fold_{i}.csv"
            df = pd.read_csv(csv_path, usecols = ["th", "accuracy"], index_col = None)
            acc_list.append(df["accuracy"][0])

        if mode == "default":
            median_default = statistics.median(acc_list)
        elif mode == "constant":
            median_constant = statistics.median(acc_list)
        elif mode == "tiktok":
            median_tiktok = statistics.median(acc_list)
        else:
            print(f"mode: {mode} invalid")
            return

    return (median_default, median_constant, median_tiktok)
