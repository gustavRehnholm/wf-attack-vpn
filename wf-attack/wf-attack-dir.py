#!/usr/bin/python3

'''
wf attack on all files in a directory
Performed with Deep fingerprinting, on teh modes: default, constant and tiktok

python wf-attack-vpn/wf-attack/wf-attack-dir.py
'''

import os
import sys

def main():

    #DIR_MERGED     = "merged_traffic/twitch_no_offset"
    DIR_MERGED = sys.argv[1]
    # DIR_RESULT = "wf-result/twitch_no_offset"
    DIR_RESULT = sys.argv[2]

    os.system("mkdir " + DIR_RESULT)

    files = os.listdir(DIR_MERGED)

    print(files)

    # default wf attack
    for file in files:
        print(file)
        #os.system("./df-fitness.py -d " + DIR_MERGED + "--train --csv " + file + "/default.csv")

    # constant wf attack
    #for file in files:
    #    print(file)
        #os.system("./df-fitness.py -d " + DIR_MERGED + "--train --csv " + file + "/default.csv")

    # tiktok wf attack
    #for file in files:
    #    print(file)
        #os.system("./df-fitness.py -d " + DIR_MERGED + "--train --csv " + file + "/default.csv")

    return

if __name__=="__main__":
    main()