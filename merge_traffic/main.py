#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/merge_traffic/main.py
'''

# to access input from the user
import sys
# to run the script for the actually merging
from get_merged import getMerged

'''
Creates the merged traffic, used to test the WF attacks capabilities
Input:
    sys.argv[1]: the directory where the foreground dataset is stored
    sys.argv[2]: the directory where the background dataset is stored
    sys.argv[3]: the directory where the merged dataset will be stored
    sys.argv[4]: Which fold file to use, should be an integer from 0 to 9 
'''
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

    success = getMerged(dir_foreground    = DIR_FOREGROUND, 
                        dir_merged        = DIR_MERGED, 
                        dir_background    = DIR_BACKGROUND,
                        fold              = FOLD)

    if success:
        print("The merged traffic was created successfully")
    else:
        print("ERROR: the merged traffic could not be created")

    return

if __name__=="__main__":
    main()