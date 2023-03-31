#!/usr/bin/python3

'''
To run:
python wf-attack-vpn/merged_traffic/main.py
'''

import pandas as pd
import os
from merge_traffic import mergeTraffic
import shutil

'''
This program merges the inputted background and foreground traffic, and store it in the specified directory.
One can if one which to specify which fold file to use, to split the foreground traffic differently.

Input:
    dir_foreground: path to the directory that has the foreground that the background should be merged into
    dir_merged:     path to the directory where the merged result will be stored in
    dir_background: path to the directory where the background traffic is
    fold:           which fold file to use

Output:
    Boolean which tells if the program succeeded in creating the merged traffic set
'''
def getMerged(dir_foreground, dir_merged, dir_background, fold = 0):

    FOLD_CSV = dir_foreground + "/fold-" + fold + ".csv"
    key    = "df"

    # list of what each file should be used for
    foregroundTrainFiles = []
    foregroundValidFiles = []
    foregroundTestFiles  = []
    mergedTrainFiles = []
    mergedValidFiles = []
    mergedTestFiles  = []

    # clean old results if their is any
    if os.path.exists(dir_merged):
        shutil.rmtree(dir_merged)
    os.mkdir(dir_merged)
    
    # The naming structure between the foreground and the merged should be the same
    for (dirpath, dirnames, filenames) in os.walk(dir_foreground, topdown=True):
        for dirs in dirnames:
            curr_path = os.path.join(dir_merged, dirs)
            if not os.path.exists(os.path.join(dir_merged, dirs)):
                os.mkdir(curr_path)


    # dataframe representation of what each foreground file should be used for
    df_fold = pd.read_csv(FOLD_CSV)
    #FOLD_DF_ATTR = ['log', 'is_train', 'is_valid', 'is_test']
    #dfFiles = df_fold[FOLD_DF_ATTR]

    # For every log file in the web traffic, make sure that there is an correlating log file to store the parsed result
    for x in range(0, len(df_fold['log'])):
        if(df_fold['is_train'][x] == True): 
            mergedTrainFiles.append(os.path.join(dir_merged, df_fold['log'][x]))
            foregroundTrainFiles.append(os.path.join(dir_foreground, "client", df_fold['log'][x]))

        elif(df_fold['is_valid'][x] == True): 
            mergedValidFiles.append(os.path.join(dir_merged, df_fold['log'][x]))
            foregroundValidFiles.append(os.path.join(dir_foreground, "client", df_fold['log'][x]))

        elif(df_fold['is_test'][x] == True): 
            mergedTestFiles.append(os.path.join(dir_merged, df_fold['log'][x]))
            foregroundTestFiles.append(os.path.join(dir_foreground, "client", df_fold['log'][x]))

        else:
            print("ERROR: the file " + df_fold['log'][x] + "does not have a determined usage")
            print("Aborting program")
            return

    # get size of the background traffic
    store = pd.HDFStore(dir_background)
    df_len = store.get_storer(key).nrows
    store.close()
    # divide it up in 10 parts, 
    part_of_10 = round(df_len/10)

    print("Size of the background")
    print(df_len)

    
    if not mergeTraffic(mergedTestFiles , foregroundTestFiles , dir_background, 0              , part_of_10):
        return False
    if not mergeTraffic(mergedValidFiles, foregroundValidFiles, dir_background, part_of_10 + 1 , part_of_10*2):
        return False
    if not mergeTraffic(mergedTrainFiles, foregroundTrainFiles, dir_background, part_of_10*2 + 1, int(df_len)):
        return False
    '''
    if not mergeTraffic(mergedTestFiles , foregroundTestFiles , dir_background, 0              , int(df_len)):
        return False
    if not mergeTraffic(mergedValidFiles, foregroundValidFiles, dir_background, 0              , int(df_len)):
        return False
    if not mergeTraffic(mergedTrainFiles, foregroundTrainFiles, dir_background, 0              , int(df_len)):
        return False
    '''
    print("Succeeded in creating the merged traffic set")
    return True

if __name__=="__main__":
    main()