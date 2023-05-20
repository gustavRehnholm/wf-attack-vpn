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
    

    path = f"wf_result/{result}/{app}"
    if not os.path.exists(path):
        os.makedirs(path)

    for mode in modes:
        # create path to the figure path
        path = f"wf_result/{result}/{app}/{mode}"
        if not os.path.exists(path):
            os.makedirs(path)

        # for every fold
        for i in range(0,10):
            # copy result to the folder, for the new subgraph 
            os.system(f"cp wf_result/{in_dir}/{app}/fold_{i}/{mode}.csv wf_result/{result}/{app}/{mode}")
            # name after fold, not mode
            os.system(f"mv wf_result/{result}/{app}/{mode}/{mode}.csv wf_result/{result}/{app}/{mode}/fold_{i}.csv")
    
if __name__ == "__main__":
    main()