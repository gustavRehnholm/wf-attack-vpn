#!/usr/bin/env python3

import argparse
import os
from combine_10fold_undef_attack import combine_10fold_undef_attack
from print_struct import print_struct

'''
To run:
python wf-attack-vpn/train_test_combinations/undef/combine_undef_app.py --app netflix
'''

ap = argparse.ArgumentParser()

ap.add_argument("--app"   , required = True , type = str, default = "", 
    help="Which dataset (which uses the application) should be attacked")

args = ap.parse_args()

def main():

    # create the new merged dataset
    # os.system(f"python wf-attack-vpn/train_test_combinations/undef/combine_10fold_undef.py --app {args.app}")

    # WF attack on the new set
    combine_10fold_undef_attack(args.app)

    # print structure
    print_struct(dir_input = f"wf_result/combined_undef/{args.app}", dir_result = f"wf_result/combined_undef_print/{args.app}")

    # overhead (only to confirm that the dataset is reasonable)
    #os.system(f"python wf-attack-vpn/data_analysis/merged_analysis/analyze_all_merged.py -i merged_traffic/combined/foreground/{args.app} -r overhead/combine_undef/{args.app}")

    # rm the combined dataset
    # os.system(f"rm -f -r merged_traffic/combined/foreground/{args.app}")

if __name__ == "__main__":
    main()