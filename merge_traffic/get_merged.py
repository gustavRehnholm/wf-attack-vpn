#!/usr/bin/python3

'''
TODO: fold on the background dataset

To run:
python wf-attack-vpn/merged_traffic/main.py
'''

import pandas as pd
import os
from merge_traffic     import mergeTraffic
from merge_traffic_old import mergeTrafficOld
import shutil


def getMerged(dir_foreground, dir_merged, dir_background, f_fold = 0, b_fold = 0, workers = 5):
    '''
    This program merges the inputted background and foreground traffic, and store it in the specified directory.

    Args:
        dir_foreground - Required : path to the directory that has the foreground that the background should be merged into (str)
        dir_merged     - Required : path to the directory where the merged result will be stored in                         (str)
        dir_background - Required : path to the directory where the background traffic is                                   (str)
        f_fold         - Optional : which fold file to use for the foreground [0, 9] (default = 0)                          (int)
        b_fold         - Optional : which fold to use for the background [0, 9] (default = 0) NOT IMPLEMENTED               (int)
        workers        - Optional : number of workers, multiprocessing (default = 5)                                        (int)
    Output:
        Boolean which tells if the program succeeded in creating the merged traffic set                                     (bool)
    '''

    FOLD_CSV = dir_foreground + "/fold-" + str(f_fold) + ".csv"
    KEY      = "df"

    # list of what each file should be used for
    foreground_train_files = []
    foreground_valid_files = []
    foreground_test_files  = []
    merged_train_files = []
    merged_valid_files = []
    merged_test_files  = []

    # clean old results if their is any
    if os.path.exists(dir_merged):
        shutil.rmtree(dir_merged)
    os.mkdir(dir_merged)
    
    # The naming structure between the foreground and the merged should be the same
    for (dirpath, dirnames, filenames) in os.walk(dir_foreground, topdown = True):
        for dirs in dirnames:
            curr_path = os.path.join(dir_merged, dirs)
            if not os.path.exists(os.path.join(dir_merged, dirs)):
                os.mkdir(curr_path)

    df_fold = pd.read_csv(FOLD_CSV)

    # For every log file in the foreground, make sure that there is an correlating log file to store the parsed result
    for x in range(0, len(df_fold['log'])):
        if(df_fold['is_train'][x] == True): 
            merged_train_files.append(os.path.join(dir_merged, df_fold['log'][x]))
            foreground_train_files.append(os.path.join(dir_foreground, "client", df_fold['log'][x]))

        elif(df_fold['is_valid'][x] == True): 
            merged_valid_files.append(os.path.join(dir_merged, df_fold['log'][x]))
            foreground_valid_files.append(os.path.join(dir_foreground, "client", df_fold['log'][x]))

        elif(df_fold['is_test'][x] == True): 
            merged_test_files.append(os.path.join(dir_merged, df_fold['log'][x]))
            foreground_test_files.append(os.path.join(dir_foreground, "client", df_fold['log'][x]))

        else:
            print("ERROR: the file " + df_fold['log'][x] + "does not have a determined usage")
            print("Aborting program")
            return

    # get number of packets in the background traffic
    store = pd.HDFStore(dir_background)
    df_len = store.get_storer(KEY).nrows
    store.close()
    # divide it up in 10 parts, 
    part_of_10 = round(df_len/10)
    print(f"Size of the background: {df_len}")
    
    if workers == 1:
        # start with the training files, if the program has difficulties in running, it will crash at the training
        print("Start merging train files")
        if not mergeTrafficOld(merged_train_files, foreground_train_files, dir_background, part_of_10*2 + 1, int(df_len)):
            return False
        print("Start merging test files")
        if not mergeTrafficOld(merged_test_files , foreground_test_files , dir_background, 0              , part_of_10):
            return False
        print("Start merging validation files")
        if not mergeTrafficOld(merged_valid_files, foreground_valid_files, dir_background, part_of_10 + 1 , part_of_10*2):
            return False
    else:
        # start with the training files, if the program has difficulties in running, it will crash at the training
        print("Start merging train files")
        if not mergeTraffic(merged_train_files, foreground_train_files, dir_background, part_of_10*2 + 1, int(df_len), workers):
            return False
        print("Start merging test files")
        if not mergeTraffic(merged_test_files , foreground_test_files , dir_background, 0              , part_of_10, workers):
            return False
        print("Start merging validation files")
        if not mergeTraffic(merged_valid_files, foreground_valid_files, dir_background, part_of_10 + 1 , part_of_10*2, workers):
            return False

    '''
    if workers == 1:
        # start with the training files, if the program has difficulties in running, it will crash at the training
        print("Start merging train files")
        if not mergeTrafficOld(mergedTrainFiles, foregroundTrainFiles, dir_background, 0, int(df_len)):
            return False
        print("Start merging test files")
        if not mergeTrafficOld(mergedTestFiles , foregroundTestFiles , dir_background, 0, int(df_len)):
            return False
        print("Start merging validation files")
        if not mergeTrafficOld(mergedValidFiles, foregroundValidFiles, dir_background, 0, int(df_len)):
            return False
    else:
        # start with the training files, if the program has difficulties in running, it will crash at the training
        print("Start merging train files")
        if not mergeTraffic(mergedTrainFiles, foregroundTrainFiles, dir_background, 0, int(df_len), workers):
            return False
        print("Start merging test files")
        if not mergeTraffic(mergedTestFiles , foregroundTestFiles , dir_background, 0, int(df_len), workers):
            return False
        print("Start merging validation files")
        if not mergeTraffic(mergedValidFiles, foregroundValidFiles, dir_background, 0, int(df_len), workers):
            return False
    '''
    print("Succeeded in creating the merged traffic set")
    return True

if __name__=="__main__":
    main()