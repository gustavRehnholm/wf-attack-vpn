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
ap.add_argument("-l", required=False, default=False,
    action="store_true", help="large (10k) input length, else 5k")
args = vars(ap.parse_args())

def main():
    '''
    wf attack on all files in a directory
    Performed with Deep fingerprinting, on the modes: default, constant and Tik-Tok
    It have support for multiprocessing, but needs a good computer to make use of it
    '''

    # create the path for the result
    splitted_merged_path = os.path.dirname(args['r'])
    os.system("mkdir " + splitted_merged_path)
    os.system("rm -f -r " + args['r'])
    os.system("mkdir " + args['r'])
    
    start_time = timeit.default_timer()

    df_attack(args['m'], args['s'], ""          , args['epochs'], args['r'], "default", args['l'])
    df_attack(args['m'], args['s'], "--constant", args['epochs'], args['r'], "constant", args['l'])
    df_attack(args['m'], args['s'], "--tiktok"  , args['epochs'], args['r'], "tiktok", args['l'])

    end_time = timeit.default_timer()
    runtime_min = (end_time - start_time)/60
    print(f"runtime for this merged dataset(min): {runtime_min:.1f}")
    return


def df_attack(dir_merged, sample, mode, epochs, dir_result, name, len10k):
    '''
    Run a DF attack with the provided input
    Args:
        dir_merged - Required : Path to the merged dataset                  (str)
        sample     - Required : Number of samples                           (str)
        mode       - Required : Mode used "default", "constant" or "tiktok" (str)
        epochs     - Required : epochs to run                               (str)
        dir_result - Required : Path where the result will be stored        (str)
        name       - Required : File name of the result                     (str)
        len10k     - Required : if one should use 10k packet per file (bool)
    '''
    if len10k:
        len = "-l"
    else:
        len = ""

    txt = f"./df-fitness-wg.py -d {dir_merged} --train -s {sample} {mode} --epochs {epochs} {len} --csv {dir_result}/{name}.csv"
    os.system(txt)


if __name__=="__main__":
    main()