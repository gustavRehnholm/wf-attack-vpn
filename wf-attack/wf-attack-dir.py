#!/usr/bin/python3

'''
wf attack on all files in a directory


python wf-attack-vpn/wf-attack/wf-attack-dir.py
'''

import os
import sys

def main():

    #dir_merged = sys.argv[1]

    dir_merged = "merged_traffic/twitch_no_offset"

    files 



    # ./df-fitness.py -d merged_traffic/twitch_small_offset_30_60_0 --train --csv wf-result/twitch_small_offset_30_60_0/twitch_default.csv
    DIR_FOREGROUND = input("Where is the foreground located?")
    DIR_BACKGROUND = input("Where is the background located?")
    DIR_MERGED     = input("Where should the merged traffic be stored")

    
    amount = int(input("How large part of the background traffic should be used? (1/input packets will be used)"))
    if type(amount) is int:
        BACKGROUND_AMOUNT = amount
    else:
        print("the provided value is not an integer, aborting the program ")
        return


    #DIR_FOREGROUND = "foreground_traffic"
    #DIR_MERGED     = "merged_traffic/twitch_no_offset"

    #DIR_ALL_BACKGROUNDS = "background_traffic"
    #FILE_BACKBROUND     = "twitch.h5"
    #DIR_BACKGROUND      = DIR_ALL_BACKGROUNDS + "/" + FILE_BACKBROUND

    #BACKGROUND_AMOUNT = 1

    generateMergedTraffic(dir_foreground = DIR_FOREGROUND, dir_merged = DIR_MERGED, dir_background = DIR_BACKGROUND, background_amount = BACKGROUND_AMOUNT)

if __name__=="__main__":
    main()