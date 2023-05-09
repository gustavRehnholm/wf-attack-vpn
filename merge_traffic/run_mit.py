#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/merge_traffic/run_mit.py -app ...
'''

ap = argparse.ArgumentParser()
ap.add_argument("-app"   , required = True , type = str, default = "", 
    help="MIT application to use")
args = vars(ap.parse_args())

def main():
    '''
    10-fold merge for an MIT application
    '''

    app = args["app"]

    for i in range(0,10):
        os.system(f"python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/{app}.h5 -m merged_traffic/mit/{app}_{i} --bfold {i} -w 10")
    
if __name__ == "__main__":
    main()