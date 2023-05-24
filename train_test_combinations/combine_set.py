#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/wf-attack/train_test_combinations/combine_undef_app.py --app vimeo
'''

ap = argparse.ArgumentParser()

ap.add_argument("--train"   , required = True , type = str, default = "", 
    help="...")
ap.add_argument("--test"   , required = True , type = str, default = "", 
    help="...")
ap.add_argument("--result"   , required = True , type = str, default = "", 
    help="...")

args = ap.parse_args()

def main():

    # create the new merged dataset
    os.system(f"python wf-attack-vpn/train_test_combinations/combine_10fold_set.py --app {args.app}")
    # WF attack on the new set
    os.system(f"python wf-attack-vpn/train_test_combinations/combine_10fold_undef_attack.py --app {args.app}")
    # print structure

    # rm old merged

if __name__ == "__main__":
    main()