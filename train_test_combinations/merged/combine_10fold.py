#!/usr/bin/python3

import os
from combine import combine

def combine_10fold(train_dir, test_dir, title, f_fold = 0, workers = 10):
    '''
    Args:
        f_fold    - Optional : which fold file to use for the foreground [0, 9]   (int)
        workers   - Optional : number of workers, multiprocessing                 (int)
    '''
    os.system(f"mkdir merged_traffic/combined/merged/{title}")

    for i in range(10):
        print(f"{title}: fold {i}")

        os.system(f"mkdir merged_traffic/combined/merged/{title}/fold_{i}")

        combine(dir_train = f"{train_dir}/fold_{i}", 
                dir_test = f"{test_dir}/fold_{i}", 
                dir_dest = f"merged_traffic/combined/merged/{title}/fold_{i}")

    return