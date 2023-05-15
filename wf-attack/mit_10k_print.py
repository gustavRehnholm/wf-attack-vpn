#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/wf-attack/mit_10k_print.py --app youtube -r mit_10k_print -i mit_10k
'''

ap = argparse.ArgumentParser()
ap.add_argument("-r"   , required = True , type = str, default = "", 
    help="dir inside wf_result to store the result")
ap.add_argument("-i"   , required = True , type = str, default = "", 
    help="dir inside wf_result to copy from")
ap.add_argument("--app"   , required = True , type = str, default = "", 
    help="MIT application to use")
args = vars(ap.parse_args())

def main():
    '''
    create structure to print the 10-fold result
    '''
    print("Start wf attack on 10-fold")

    app = args["app"]
    result = args["r"]
    in_dir = args["i"]
    modes = ["default", "constant", "tiktok"]
    
    os.system(f"mkdir wf_result/{dir}/{app}")
    for mode in modes:
        # create path to the figure path
        os.system(f"mkdir wf_result/{dir}/{app}/mode")
        # for every fold
        for i in range(0,10):
            os.system(f"cp wf_result/{in_dir}/{app}/fold_{i}/{mode}.csv wf_result/{dir}/{app}/{mode}/fold_{i}.csv")
    
if __name__ == "__main__":
    main()