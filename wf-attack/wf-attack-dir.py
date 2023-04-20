#!/usr/bin/python3

import argparse
import os
import sys
from multiprocessing import Pool
import timeit

ap = argparse.ArgumentParser()
ap.add_argument("-m", required=True, default="", help="root folder of the merged dataset")
ap.add_argument("-r", required=True, default="", help="root folder of the df result")
ap.add_argument("-s", required=False, type=int, default=100,
    help="sample to use (100 in total)")
args = vars(ap.parse_args())

def main():
    '''
    wf attack on all files in a directory
    Performed with Deep fingerprinting, on the modes: default, constant and Tik-Tok
    It have support for multiprocessing, but needs a good computer to make use of it
    '''

    DIR_MERGED = args['m']
    DIR_RESULT = args['r']
    SAMPLE     = args['s']

    # create the path for the result
    splitted_merged_path = os.path.dirname(DIR_RESULT)
    os.system("mkdir " + splitted_merged_path)
    os.system("rm -f -r " + DIR_RESULT)
    os.system("mkdir " + DIR_RESULT)
    
    input = [
        (DIR_MERGED, SAMPLE, ""          , DIR_RESULT, "default"),
        (DIR_MERGED, SAMPLE, "--constant", DIR_RESULT, "constant"),
        (DIR_MERGED, SAMPLE, "--tiktok"  , DIR_RESULT, "tiktok")
    ]
    start_time = timeit.default_timer()
    p = Pool(1)
    p.starmap(df_attack, input)

    end_time = timeit.default_timer()
    print(f"runtime for this merged dataset: {end_time - start_time}")
    return

def df_attack(dir_merged, sample, mode, dir_result, name):
    txt = f"./df-fitness.py -d {dir_merged} --train -s {sample} {mode} --csv {dir_result}/{name}.csv"
    os.system(txt)

if __name__=="__main__":
    main()