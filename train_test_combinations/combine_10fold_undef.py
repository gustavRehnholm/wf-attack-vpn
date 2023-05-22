#!/usr/bin/python3

import pandas as pd
import os
import shutil
from multiprocessing import Pool
import argparse
from combine import combine

ap = argparse.ArgumentParser()
ap.add_argument("--app"   , required = True , type = str, default = "", 
    help="Root folder to the merged dataset to use for training and validation")
args = ap.parse_args()


def main():
    combine_10fold(app = args.app)
    return

def combine_10fold(app, f_fold = 0, workers = 10):
    '''
    Args:
        app       - Required : application to test against foreground             (str)
        f_fold    - Optional : which fold file to use for the foreground [0, 9]   (int)
        workers   - Optional : number of workers, multiprocessing                 (int)
    '''
    os.system(f"merged_traffic/combined/foreground/{app}")
    for i in range(10):
        print(f"{app}: fold {i}")
        os.system(f"merged_traffic/combined/foreground/{app}/fold_{i}")
        combine(dir_train = "foreground_traffic", 
                dir_test = f"merged_traffic/mit_5k/{app}/fold_{i}", 
                dir_dest = f"merged_traffic/combined/foreground/{app}/fold_{i}")

        #os.system(f"python wf-attack-vpn/train_test_combinations/combine.py --train foreground_traffic --test merged_traffic/mit_5k/{app}/fold_{i} --dest merged_traffic/combined/foreground/{app}/fold_{i}")

if __name__=="__main__":
    main()