#!/usr/bin/python3

'''
This program creates the merged traffic, used to test the WF attacks capabilities

TODO:
Input (sys.argv):
[1] : chunk size
[2] : offsett for the test files
[3] : offset for the valid files
[4] : offset for the train files
[5] : directory for the foreground traffic to use
[6] : directory for the merged traffic to use
[7] : directory for the background traffic file to use

python wf-attack-vpn/generate_merged_dataset/main.py
'''

import sys
from generate_merged_traffic import generateMergedTraffic

def main():

    DIR_FOREGROUND = sys.argv[1]
    DIR_BACKGROUND = sys.argv[2]
    DIR_MERGED     = sys.argv[3]
    
    amount = int(sys.argv[4])
    if type(amount) is int:
        BACKGROUND_AMOUNT = amount
    else:
        print("the provided value is not an integer, aborting the program ")
        return

    generateMergedTraffic(dir_foreground = DIR_FOREGROUND, dir_merged = DIR_MERGED, dir_background = DIR_BACKGROUND, background_amount = BACKGROUND_AMOUNT)

if __name__=="__main__":
    main()