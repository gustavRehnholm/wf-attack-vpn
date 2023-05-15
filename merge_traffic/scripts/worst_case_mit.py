#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app vimeo

# merge the applications, so that one can be generated for the worst case
python wf-attack-vpn/merge_traffic/main.py -f netflix -b background_traffic/mit/vimeo.h5 -m merged_traffic/worst_case --bfold  
'''

ap = argparse.ArgumentParser()
ap.add_argument("--app"   , required = True , type = str, default = "")
args = vars(ap.parse_args())

def main():
    '''
    10-fold merge for an MIT application
    '''

    app = args["app"]

    for i in range(0,10):
        os.system(f"mkdir merged_traffic/worst_case/fold_{i}")
        os.system(f"python wf-attack-vpn/merge_traffic/main.py -f merged_traffic/mit/youtube/fold_{i} -b background_traffic/mit/{app}.h5 -m merged_traffic/worst_case/fold_{i} --bfold {i}")
    
if __name__ == "__main__":
    main()