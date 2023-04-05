#!/usr/bin/python3

'''
wf attack on all files in a directory
Performed with Deep fingerprinting, on teh modes: default, constant and Tik-Tok

TODO: Stop program if it can not create the result dir
TODO: check that the input paths exists

python wf-attack-vpn/wf-attack/wf-attack-dir.py
'''

import os
import sys

def main():

    DIR_MERGED = sys.argv[1]
    DIR_RESULT = sys.argv[2]
    SAMPLE     = sys.argv[3]

    # create the path for the result
    splitted_merged_path = os.path.dirname(DIR_RESULT)
    os.system("mkdir " + splitted_merged_path)
    os.system("rm -f -r " + DIR_RESULT)
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