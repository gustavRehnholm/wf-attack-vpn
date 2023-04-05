#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/merge_traffic/main.py
'''

import sys
from get_merged import getMerged
import timeit


def main():
    '''
    Creates the merged traffic, used to test the WF attacks capabilities

    Args:
        sys.argv[1]  - Required : the directory where the foreground dataset is stored
        sys.argv[2]  - Required : the directory where the background dataset is stored
        sys.argv[3]  - Required : the directory where the merged dataset will be stored
        sys.argv[4]  - Required : Which fold file to use, should be an integer from 0 to 9 
    '''

    DIR_FOREGROUND = sys.argv[1]
    print("Chosen foreground")
    print(sys.argv[1])
    DIR_BACKGROUND = sys.argv[2]
    print("Chosen background")
    print(sys.argv[2])
    DIR_MERGED     = sys.argv[3]
    print("Chosen merged")
    print(sys.argv[3])
    FOLD           = sys.argv[4]
    print("Chosen fold")
    print(sys.argv[4])

    start_time = timeit.default_timer()

    success = getMerged(dir_foreground    = DIR_FOREGROUND, 
                        dir_merged        = DIR_MERGED, 
                        dir_background    = DIR_BACKGROUND,
                        fold              = FOLD)
    end_time = timeit.default_timer()
    if success:
        print("The merged traffic was created successfully")
    else:
        print("ERROR: the merged traffic could not be created")
    runtime_min = (end_time - start_time) / 60 
    print("Runtime: " + str(runtime_min))

    return

if __name__=="__main__":
    main()