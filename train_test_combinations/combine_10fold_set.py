#!/usr/bin/python3

import pandas as pd
import os
import shutil
from multiprocessing import Pool
from combine import combine

def combine_10fold_Set(dir_train, dir_test, dir_result, f_fold = 0, workers = 10):
    '''
    Args:
        app       - Required : application to test against foreground             (str)
        f_fold    - Optional : which fold file to use for the foreground [0, 9]   (int)
        workers   - Optional : number of workers, multiprocessing                 (int)
    '''
    os.system(f"mkdir dir_result")

    for i in range(10):
        print(f"{dir_result}: fold {i}")
        os.system(f"mkdir {dir_result}/fold_{i}")

        combine(dir_train = f"{dir_train}/fold_{i}", 
                dir_test = f"{dir_test}/fold_{i}", 
                dir_dest = f"{dir_result}/fold_{i}")

    return
    
if __name__=="__main__":
    main()