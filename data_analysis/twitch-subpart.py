#!/usr/bin/python3

import pandas as pd
import os
import shutil


# python wf-attack-vpn/data_analysis/twitch-subpart.py

def main():
    '''
    create a subpart of the Twitch dataset, for analysis
    '''

    print("Start creating subpart of the Twitch captures")

    # All usable captures
    DIR_INPUT = "captures_clean"
    # the 50 largest captures
    DIR_OUTPUT = "captures_50"

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir "    + DIR_OUTPUT)

    # list of all twitch traffic captures files, sorted by size
    files        = os.listdir(DIR_INPUT)
    sorted_files = sorted(files, key =  lambda x: os.stat(os.path.join(DIR_INPUT, x)).st_size)
    sorted_files = list(reversed(sorted_files))
    files_len    = len(sorted_files)

    index = 0

    for file in sorted_files:
        index += 1
        filename = os.fsdecode(file)
        
        if index >= 30 and index < 80:
            print("")
            print("Include file " + str(index) + "/" + str(files_len) + ": " + str(filename))
            print("")

            src = DIR_INPUT  + "/" + filename
            dst = DIR_OUTPUT + "/" + filename
            shutil.copyfile(src, dst)

        # to gather a subset
        if index >= 80:
            break

    print("Have created a subset of Twitch data, store in " + DIR_OUTPUT)

# run main 
if __name__=="__main__":
    main()