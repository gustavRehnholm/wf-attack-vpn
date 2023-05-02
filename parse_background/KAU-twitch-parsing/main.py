#!/usr/bin/python3

import argparse
import timeit
# own defined
from log_2_h5           import log_2_h5
from rm_broken_captures import rm_broken_captures
from parse_background   import parse_background
from merge_parsed_noise import merge_parsed_noise
from analyze_dataset    import analyze_dataset

'''
TODO: progressbar for the different steps that works with multiprocessing
'''

'''
To run:
python wf-attack-vpn/parse_background/KAU-twitch-parsing/main.py
'''

ap = argparse.ArgumentParser()
ap.add_argument("-w"     , required = False, default = 10 , type = int, help = "number of workers (multiprocessing)")
args = vars(ap.parse_args())

def main():
    '''
    Parse the Twitch dataset from rds-collect
    '''

    start_time = timeit.default_timer()

    # conver the log files to h5 format
    log_2_h5(workers = args['w'])
    # rm the capture files that are determined to be broken
    rm_broken_captures(workers = args['w'])
    # parse the usable capture files
    parse_background(workers = args['w'])
    # analyze the usable capture files
    analyze_dataset(workers = args['w'])
    # merge the parsed capture files to one background dataset to use
    merge_parsed_noise()

    end_time = timeit.default_timer()
        
    runtime_min = (end_time - start_time) / 60 
    print(f"Runtime(min): {runtime_min:.1f}")

    return

if __name__=="__main__":
    main()