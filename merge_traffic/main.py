#!/usr/bin/python3

import argparse
import timeit
# own defined
from get_merged import getMerged


ap = argparse.ArgumentParser()
ap.add_argument("-f"    , required = True , default = "", type = str, help = "root folder of the foreground dataset")
ap.add_argument("-b"    , required = True , default = "", type = str, help = "root folder of the background dataset")
ap.add_argument("-m"    , required = True , default = "", type = str, help = "root folder of the merged dataset")
ap.add_argument("--fold", required = False, default = 0 , type = int, help = "fold file to use [0,9]", choices = range(0, 10))
ap.add_argument("-w"    , required = False, default = 5 , type = int, help = "number of workers (multiprocessing)")
args = vars(ap.parse_args())

def main():
    '''
    Creates the merged traffic, used to test DF and TikTok attacks capabilities
    '''
    DIR_FOREGROUND = args['f']
    DIR_BACKGROUND = args['b']
    DIR_MERGED     = args['m']
    FOLD           = args['fold']
    WORKERS        = args['w']

    print(WORKERS)
    return

    start_time = timeit.default_timer()
    success = getMerged(dir_foreground = DIR_FOREGROUND, 
                        dir_merged     = DIR_MERGED, 
                        dir_background = DIR_BACKGROUND,
                        fold           = FOLD,
                        workers        = WORKERS)
    end_time = timeit.default_timer()

    if success:
        print("The merged traffic was created successfully")
    else:
        print("ERROR: the merged traffic could not be created")
        
    runtime_min = (end_time - start_time) / 60 
    print("Runtime(min): " + str(runtime_min))

    return

if __name__=="__main__":
    main()