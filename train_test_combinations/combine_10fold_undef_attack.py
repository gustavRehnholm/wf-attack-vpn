#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/wf-attack/train_test_combinations/combine_wf_attack.py --app vimeo
'''

ap = argparse.ArgumentParser()

ap.add_argument("--app"   , required = True , type = str, default = "", 
    help="Which dataset (which uses the application) should be attacked")

args = ap.parse_args()

def main():

    print("Start wf attack on combined 10-fold")

    os.system(f"mkdir wf_result/combine_undef/{args.app}")
    for i in range(0,10):
        os.system(f"mkdir wf_result/combine_undef/{args.app}/fold_{i}")
        os.system(f"python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/combined/foreground/{args.app}/fold_{i}/client -r wf_result/combine_undef/{args.app}/fold_{i} -s 100 --epochs 30")
    
if __name__ == "__main__":
    main()