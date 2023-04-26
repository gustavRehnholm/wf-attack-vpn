#!/usr/bin/python3

import argparse
import os
import sys
from multiprocessing import Pool
import timeit

ap = argparse.ArgumentParser()
ap.add_argument("-m", required = True , type = str, default = "" , 
    help = "root folder of the merged dataset")
ap.add_argument("-r", required = True , type = str, default = "" , 
    help = "root folder of the df result")
ap.add_argument("-s", required = False, type = int, default = 100,
    help = "sample to use (100 in total)")
ap.add_argument("-w", required = False, type = int, default = 10,
    help = "Number of workers (multiprocessing) NOT IMPLEMENTED")
ap.add_argument("--epochs", required = False, type = int, default = 30,
    help="the number of epochs for training")
args = vars(ap.parse_args())

def main():
    '''
    wf attack on all files in a directory
    Performed with Deep fingerprinting, on the modes: default, constant and Tik-Tok
    It have support for multiprocessing, but needs a good computer to make use of it
    '''

    # create the path for the result
    splitted_merged_path = os.path.dirname(DIR_RESULT)
    os.system("mkdir " + splitted_merged_path)
    os.system("rm -f -r " + DIR_RESULT)
    os.system("mkdir " + DIR_RESULT)
    
    start_time = timeit.default_timer()

    df_attack(args['m'], args['s'], ""          , args['epochs'], args['r'], "default")
    df_attack(args['m'], args['s'], "--constant", args['epochs'], args['r'], "constant")
    df_attack(args['m'], args['s'], "--tiktok"  , args['epochs'], args['r'], "tiktok")

    end_time = timeit.default_timer()
    print(f"runtime for this merged dataset: {end_time - start_time}")
    return


def df_attack(dir_merged, sample, mode, epochs, dir_result, name):
    '''
    Run a DF attack with the provided input
    Args:
        dir_merged - Required : Path to the merged dataset                  (str)
        sample     - Required : Number of samples                           (str)
        mode       - Required : Mode used "default", "constant" or "tiktok" (str)
        epochs     - Required : epochs to run                               (str)
        dir_result - Required : Path where the result will be stored        (str)
        name       - Required : File name of the result                     (str)
    '''
    txt = f"./df-fitness.py -d {dir_merged} --train -s {sample} {mode} --epochs {epochs} --csv {dir_result}/{name}.csv"
    os.system(txt)


if __name__=="__main__":
    main()