#!/usr/bin/python3

'''
This program creates the merged traffic, used to test the WF attacks capabilities

python wf-attack-vpn/merge_traffic/main.py
'''

import sys
from get_merged import getMerged

def main():

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

    getMerged(dir_foreground    = DIR_FOREGROUND, 
              dir_merged        = DIR_MERGED, 
              dir_background    = DIR_BACKGROUND,
              fold              = FOLD)

if __name__=="__main__":
    main()