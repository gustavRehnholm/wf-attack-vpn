#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/wf-attack/worst_case_print.py --app youtube -r mit_10k_print -i mit_10k
'''

ap = argparse.ArgumentParser()

# worst_case_print_10k or worst_case_print_5k
ap.add_argument("-r"   , required = True , type = str, default = "", 
    help="dir inside wf_result to store the result")

# worst_case_10k or worst_case_5k
ap.add_argument("-i"   , required = True , type = str, default = "", 
    help="dir inside wf_result to copy from")

args = vars(ap.parse_args())

def main():
    '''
    create structure to print the 10-fold result
    '''
    print("Start creating a printable 10-fold result")

    result = args["r"]
    in_dir = args["i"]
    modes = ["default", "constant", "tiktok"]
    

    path = f"wf_result/{result}"
    if not os.path.exists(path):
        os.makedirs(path)

    for mode in modes:
        # create path to the figure path
        path = f"wf_result/{result}/{mode}"
        if not os.path.exists(path):
            os.makedirs(path)

        # for every fold
        for i in range(0,10):
            # copy result to the folder, for the new subgraph 
            os.system(f"cp wf_result/{in_dir}/fold_{i}/{mode}.csv wf_result/{result}/{mode}")
            # name after fold, not mode
            os.system(f"mv wf_result/{result}/{mode}/{mode}.csv wf_result/{result}/{mode}/fold_{i}.csv")
    
if __name__ == "__main__":
    main()