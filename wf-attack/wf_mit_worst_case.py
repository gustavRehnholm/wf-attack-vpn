#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/wf-attack/wf_mit_worst_case.py --len10k True
'''

ap = argparse.ArgumentParser()
ap.add_argument("--len10k"   , required = False , type = bool, default = False, 
    help="How many packets per file to train for")
args = vars(ap.parse_args())

def main():
    '''
    wf-attack 10-fold merge for an MIT worst case scenario (support both 5k and 10k packets per file)
    '''
    print("Start wf attack on 10-fold")

    if args["len10k"]:
        len = "-l"
        txt = "worst_case_10k"
    else:
        len = ""
        txt = "worst_case_5k"

    os.system(f"mkdir wf_result/{txt}")
    for i in range(0,10):
        os.system(f"mkdir wf_result/{txt}/fold_{i}")
        os.system(f"python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/worst_case_b/fold_{i}/client -r wf_result/{txt}/fold_{i} -s 100 --epochs 30 {len}")
    
if __name__ == "__main__":
    main()