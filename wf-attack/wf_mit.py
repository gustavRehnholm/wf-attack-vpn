#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/wf-attack/wf_mit.py -app ...
'''

ap = argparse.ArgumentParser()
ap.add_argument("--app"   , required = True , type = str, default = "", 
    help="MIT application to use")
args = vars(ap.parse_args())

def main():
    '''
    wf-attack 10-fold merge for an MIT application
    '''
    print("Start wf attack on 10-fold")

    app = args["app"]

    for i in range(0,10):
        os.system(f"python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/{app}/fold_{i} -r wf_result/mit/{app}/fold_{i} -s 100 --epochs 30")
    
if __name__ == "__main__":
    main()