#!/usr/bin/env python3

import os


def print_struct(dir_input, dir_result):
    '''
    create structure to print the 10-fold result

    structure of the input and result
    dir_input/fold/mode
    dir_result/mode/fold

    Input:
        dir_input  - Required : path to data, to structure     (str)
        dir_result - Required : path where to store the result (str)
    '''
    print("Start 10-fold struct")
 
    # make sure that root folder of the result exists
    path = f"{dir_result}"
    if not os.path.exists(dir_result):
        os.makedirs(dir_result)

     
    modes = ["default", "constant", "tiktok"]
    for mode in modes:
        # make sure that each mode folder of the result exists
        path = f"{dir_result}/{mode}"
        if not os.path.exists(path):
            os.makedirs(path)

        # for every fold
        for i in range(0,10):
            # copy result to the folder, for the new subgraph 
            os.system(f"cp {dir_input}/fold_{i}/{mode}.csv {dir_result}/{mode}")
            # name after fold, not mode
            os.system(f"mv {dir_result}/{mode}/{mode}.csv {dir_result}/{mode}/fold_{i}.csv")
    
