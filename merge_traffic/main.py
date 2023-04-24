#!/usr/bin/python3

import argparse
import timeit
# own defined
from get_merged import getMerged

ap = argparse.ArgumentParser()
ap.add_argument("-f"     , required = True , default = "", type = str, help = "root folder of the foreground dataset")
ap.add_argument("-b"     , required = True , default = "", type = str, help = "root folder of the background dataset")
ap.add_argument("-m"     , required = True , default = "", type = str, help = "root folder of the merged dataset")
ap.add_argument("--ffold", required = False, default = 0 , type = int, help = "foreground fold file to use [0,9]", choices = range(0, 10))
ap.add_argument("--bfold", required = False, default = 0 , type = int, help = "background fold [0,9]", choices = range(0, 10))
ap.add_argument("-w"     , required = False, default = 5 , type = int, help = "number of workers (multiprocessing)")
args = vars(ap.parse_args())

def main():
    '''
    Creates the merged traffic, used to test DF and TikTok attacks capabilities
    '''

    start_time = timeit.default_timer()
    success = getMerged(dir_foreground = args['f'], 
                        dir_merged     = args['m'], 
                        dir_background = args['b'],
                        f_fold         = args['ffold'],
                        b_fold         = args['bfold'],
                        workers        = args['w'])
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