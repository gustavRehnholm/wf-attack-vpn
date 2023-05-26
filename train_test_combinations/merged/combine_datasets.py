#!/usr/bin/env python3

import argparse
import os

from combine_10fold        import combine_10fold
from combine_10fold_attack import combine_10fold_attack
from print_struct          import print_struct

'''
To run:
python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train ... --test ...
'''

ap = argparse.ArgumentParser()

ap.add_argument("--train"   , required = True , type = str, default = "", 
    help="")
ap.add_argument("--test"   , required = True , type = str, default = "", 
    help="")
ap.add_argument("--title"   , required = True , type = str, default = "", 
    help="")

args = ap.parse_args()

def main():

    # create the new merged dataset
    #combine_10fold(train_dir = args.train, test_dir = args.test, title = args.title) 

    # WF attack on the new set
    combine_10fold_attack(title = args.title)

    # print structure
    #print_struct(dir_input = f"wf_result/combine_merged/{args.title}", dir_result = f"wf_result/combined_merged_print/{args.title}")

    # overhead (only to confirm that the dataset is reasonable)
    #os.system(f"python wf-attack-vpn/data_analysis/merged_analysis/analyze_all_merged.py -i merged_traffic/combined/foreground/{args.app} -r overhead/combine_undef/{args.app}")

    # rm the combined dataset
    #os.system(f"rm -f -r merged_traffic/combined/merged/{args.title}")

if __name__ == "__main__":
    main()