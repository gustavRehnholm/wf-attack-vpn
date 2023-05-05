#!/usr/bin/python3

import argparse
import timeit
# own defined
from extract_dataset import extract_dataset
from parse_dataset   import parse_dataset

'''
TODO: progressbar for the different steps that works with multiprocessing
'''

'''
To run:
python wf-attack-vpn/parse_background/MIT-h5-parsing/main.py
'''

ap = argparse.ArgumentParser()
ap.add_argument("-w"     , required = False, default = 10 , type = int, help = "number of workers (multiprocessing)")
args = vars(ap.parse_args())

def main():
    '''
    Parse the Twitch dataset from rds-collect
    '''

    start_time = timeit.default_timer()

    # extract the relevant data and store them after application
    extract_dataset()
    # parse the usable capture files
    parse_dataset()

    end_time = timeit.default_timer()
        
    runtime_min = (end_time - start_time) / 60 
    print(f"Runtime(min): {runtime_min:.1f}")

    return

if __name__=="__main__":
    main()