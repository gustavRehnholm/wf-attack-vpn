#!/usr/bin/python3

'''
wf attack on all files in a directory
Performed with Deep fingerprinting, on teh modes: default, constant and tiktok

python wf-attack-vpn/wf-attack/wf-attack-dir.py
'''

import os
import sys

def main():

    DIR_MERGED = sys.argv[1]
    DIR_RESULT = sys.argv[2]
    SAMPLE     = sys.argv[3]
    
    splitted_merged_path = os.path.dirname(DIR_MERGED)

    # create the path for the result
    os.system("mkdir " + splitted_merged_path)
    os.system("mkdir " + DIR_RESULT)

    # default wf attack
    os.system("./df-fitness.py -d " + DIR_MERGED + " --train -s "+ SAMPLE +" --csv " + DIR_RESULT + "/default.csv")

    # constant wf attack
    os.system("./df-fitness.py -d " + DIR_MERGED + " --train -s "+ SAMPLE +" --constant --csv " + DIR_RESULT + "/constant.csv")

    # tiktok wf attack
    os.system("./df-fitness.py -d " + DIR_MERGED + " --train -s "+ SAMPLE +" --tiktok --csv " + DIR_RESULT + "/tiktok.csv")

    return

if __name__=="__main__":
    main()