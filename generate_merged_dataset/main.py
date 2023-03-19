#!/usr/bin/python3

'''
This program creates the merged traffic, used to test the WF attacks capabilities

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

    if sys.argv[4] == "True":
        offset = True
    elif sys.argv[4] == "False":
        offset = False
    else:
        print("invalid offset")
        print(sys.argv[4])
        return

    if sys.argv[5] == "True":
        rnd = True
    elif sys.argv[5] == "False":
        rnd = False
    else:
        print("invalid random")
        print(sys.argv[5])
        return

    if sys.argv[6] == "True":
        divide = True
    elif sys.argv[6] == "False":
        divide = False
    else:
        print("invalid divide")
        print(sys.argv[6])
        return

    generateMergedTraffic(dir_foreground    = DIR_FOREGROUND, 
                          dir_merged        = DIR_MERGED, 
                          dir_background    = DIR_BACKGROUND, 
                          background_amount = BACKGROUND_AMOUNT, 
                          offset            = offset, 
                          random            = rnd,
                          divide            = divide)

if __name__=="__main__":
    main()