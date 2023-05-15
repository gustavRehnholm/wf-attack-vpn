#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 --bfold 0
'''

import argparse
import timeit
# own defined
from get_merged import getMerged

ap = argparse.ArgumentParser()
ap.add_argument("-b"     , required = True , default = ""   , type = str, 
    help = "root folder of the background dataset")

ap.add_argument("-f"     , required = False , default = "foreground_traffic"   , type = str, 
    help = "root folder of the foreground dataset")

ap.add_argument("-m"     , required = False , default = "merged_traffic/tmp "   , type = str, 
    help = "root folder of the merged dataset")

ap.add_argument("--ffold", required = False, default = 0    , type = int, choices = range(0, 10),
    help = "foreground fold file to use [0,9]")

ap.add_argument("--bfold", required = False, default = 0    , type = int, choices = range(0, 10),
    help = "background fold [0,9]"            )
    
ap.add_argument("-w"     , required = False, default = 5    , type = int, 
    help = "number of workers (multiprocessing)")

ap.add_argument("--div"  , required = False , default = True , type = bool, 
    help = "If the background dataset should be divided among the testing, validation and training or not")

ap.add_argument("--len"  , required = False , default = 5000 , type = int, 
    help = "Number of packets per file (more efficient if it correlates to the DF attack)")

args = vars(ap.parse_args())

def main():

    print(f"Creates the merged traffic, used to test DF and TikTok attacks capabilities with {args["len"]} packets per file")

    start_time = timeit.default_timer()
    success = getMerged(dir_foreground = args['f'], 
                        dir_merged     = args['m'], 
                        dir_background = args['b'],
                        f_fold         = args['ffold'],
                        b_fold         = args['bfold'],
                        workers        = args['w'],
                        div            = args['div'],
                        file_len       = args["len"])
    end_time = timeit.default_timer()

    if success:
        print("The merged traffic was created successfully")
    else:
        print("ERROR: the merged traffic could not be created")
        
    runtime_min = (end_time - start_time) / 60 
    print(f"Runtime(min): {runtime_min:.1f}")

    return

if __name__=="__main__":
    main()