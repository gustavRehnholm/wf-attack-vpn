#!/usr/bin/python3

'''
rm the capture files that are broken (lack sufficient captures)

touch stdout/rm_broken_captures.txt
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/rm_broken_captures.py | tee stdout/rm_broken_captures.txt
'''

import pandas as pd
import os

def main():
    print("Start the removal of unusable files")

    # the captures in h5 format
    DIR_RAW_H5_NOISE = "twitch/raw_captures_h5/"
    # the usable captures
    DIR_RAW_USABLE_NOISE = "twitch/raw_usable/captures_h5/"

    COL_NAMES =  ['time', 'sender', 'receiver', 'size']


    index = 0
    for file in os.listdir(DIR_captures):

        filename = os.fsdecode(file)
        index += 1
        print("")
        print("converting file " + str(index) + "/1370: " + str(filename))
        print("")

        path = DIR_RAW_H5_NOISE + filename
        df = pd.read_hdf(path, key=key)

        for row in df:
            

# run main 
if __name__=="__main__":
    main()