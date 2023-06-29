#!/usr/bin/python3

'''
Copyright 2023 Gustav Rehnholm
SPDX-License-Identifier: Apache-2.0

To run:
python wf-attack-vpn/data_analysis/background_analysis/create_background_subset.py --start 40 --end 80
'''

import os
import shutil
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--start"     , required = True , default = 0   , type = int, 
    help = "start index")
ap.add_argument("--end"     , required = True , type = int,
    help = "end index")
args = vars(ap.parse_args())


def main():
    '''
    Create a subpart of the Twitch dataset for analysis, by providing an interval (where the files are sorted after size)
    Useful to see if an picked subset have the desired behaviors, before parsing the data. 
    '''

    print("Start creating subpart of the Twitch captures")

    # All usable captures
    DIR_INPUT = "captures_clean"
    # the 40 largest captures
    DIR_OUTPUT = "captures_40"

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
        
        if index >= args["start"] and index < args["end"]:
            print(str(filename))

            src = DIR_INPUT  + "/" + filename
            dst = DIR_OUTPUT + "/" + filename
            shutil.copyfile(src, dst)

        elif index >= args["end"]:
            break

    print("Have created a subset of Twitch data, store in " + DIR_OUTPUT)

# run main 
if __name__=="__main__":
    main()