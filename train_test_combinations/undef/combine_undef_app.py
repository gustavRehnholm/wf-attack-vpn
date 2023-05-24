#!/usr/bin/env python3

import argparse
import os
from print_struct import print_struct

'''
To run:
python wf-attack-vpn/wf-attack/train_test_combinations/combine_undef_app.py --app vimeo
'''

ap = argparse.ArgumentParser()

ap.add_argument("--app"   , required = True , type = str, default = "", 
    help="Which dataset (which uses the application) should be attacked")

args = ap.parse_args()

def main():

    # create the new merged dataset
    #os.system(f"python wf-attack-vpn/train_test_combinations/undef/combine_10fold_undef.py --app {args.app}")

    # WF attack on the new set
    #os.system(f"python wf-attack-vpn/train_test_combinations/undef/combine_10fold_undef_attack.py --app {args.app}")

    # print structure
    #print_struct(dir_input = f"wf_result/combined_undef/{args.app}", dir_result = f"wf_result/combined_undef_print/{args.app}")

    # test graph
    # python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/combined_undef_print/vimeo -w 10 -g fig/combined_undef
    os.system(f"python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/combined_undef_print/{args.app} -w 10")

    # overhead
    #os.system("python wf-attack-vpn/data_analysis/merged_analysis/analyze_all_merged.py -i merged_traffic/combined/foreground/{args.app} -r overhead/combine_undef")

    # rm the combined dataset
    #os.system(f"rm -f -r {}")

if __name__ == "__main__":
    main()