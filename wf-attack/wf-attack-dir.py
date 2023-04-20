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
from multiprocessing import Pool
import timeit

def main():

    DIR_MERGED = sys.argv[1]
    DIR_RESULT = sys.argv[2]
    SAMPLE     = sys.argv[3]

    # create the path for the result
    splitted_merged_path = os.path.dirname(DIR_RESULT)
    os.system("mkdir " + splitted_merged_path)
    os.system("rm -f -r " + DIR_RESULT)
    os.system("mkdir " + DIR_RESULT)

    
    input = [
        (DIR_MERGED, SAMPLE, ""          , DIR_RESULT, "default"),
        (DIR_MERGED, SAMPLE, "--constant", DIR_RESULT, "constant"),
        (DIR_MERGED, SAMPLE, "--tiktok"  , DIR_RESULT, "tiktok")
    ]
    start_time = timeit.default_timer()
    p = Pool(1)
    p.starmap(df_attack, input)

    '''
    # default wf attack
    os.system("./df-fitness.py -d " + DIR_MERGED + " --train -s "+ SAMPLE +" --csv " + DIR_RESULT + "/default.csv")

    # constant wf attack
    os.system("./df-fitness.py -d " + DIR_MERGED + " --train -s "+ SAMPLE +" --constant --csv " + DIR_RESULT + "/constant.csv")

    # tiktok wf attack
    os.system("./df-fitness.py -d " + DIR_MERGED + " --train -s "+ SAMPLE +" --tiktok --csv " + DIR_RESULT + "/tiktok.csv")
    '''
    end_time = timeit.default_timer()
    print(f"runtime for this merged dataset: {end_time - start_time}")
    return

def df_attack(dir_merged, sample, mode, dir_result, name):
    txt = f"./df-fitness.py -d {dir_merged} --train -s {sample} {mode} --csv {dir_result}/{name}.csv"
    os.system(txt)

if __name__=="__main__":
    main()