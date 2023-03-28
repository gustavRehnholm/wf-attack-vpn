#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

If the program runs out of primary memory during its run time, test to make the variable chunk smaller

python wf-attack-vpn/generate_merged_dataset/get_merged.py
'''

import pandas as pd
import os
from merge_traffic import mergeTraffic

'''
Input:
    dir_foreground: path to the directory that has the foreground that the background should be merged into
    dir_merged: path to the directory where the merged result will be stored in
    dir_background: path to the directory where the background traffic is
    fold:           which fold file to use
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


    print("Start the test of the merging of foreground and background traffic")

    # clean the previous result
    os.system("rm -f -r " + dir_merged)
    os.system("mkdir " + dir_merged)


    # The naming structure between the foreground and the merged should be the same
    for (dirpath, dirnames, filenames) in os.walk(dir_foreground, topdown=True):
        for dirs in dirnames:
            try: 
                os.mkdir(os.path.join(dir_merged, dirs))
            except: 
                print("File and directory exists!") 


    # dataframe representation of what each foreground file should be used for
    df = pd.read_csv(FOLD_CSV)
    FOLD_DF_ATTR = ['log', 'is_train', 'is_valid', 'is_test']
    dfFiles = df[FOLD_DF_ATTR]

    # For every log file in the web traffic, make sure that there is an correlating log file to store the parsed result
    for x in range(0, len(dfFiles['log'])):
        if(dfFiles['is_train'][x] == True): 
            mergedTrainFiles.append(os.path.join(dir_merged, dfFiles['log'][x]))
            foregroundTrainFiles.append(os.path.join(dir_foreground, "client", dfFiles['log'][x]))

        elif(dfFiles['is_valid'][x] == True): 
            mergedValidFiles.append(os.path.join(dir_merged, dfFiles['log'][x]))
            foregroundValidFiles.append(os.path.join(dir_foreground, "client", dfFiles['log'][x]))

        elif(dfFiles['is_test'][x] == True): 
            mergedTestFiles.append(os.path.join(dir_merged, dfFiles['log'][x]))
            foregroundTestFiles.append(os.path.join(dir_foreground, "client", dfFiles['log'][x]))

        else:
            print("ERROR: the file " + dfFiles['log'][x] + "does not have a determined usage")
            print("Aborting program")
            return

    # get size of the background traffic
    store = pd.HDFStore(dir_background)
    df_len = store.get_storer(key).nrows
    store.close()
    # make it smaller for testing
    df_len = round(df_len / background_amount)
    # divide it up in 10 parts, 
    part_of_10 = round(df_len/10)

    print("Size of the background")
    print(df_len)

    if not mergeTraffic(mergedTestFiles , foregroundTestFiles , dir_background, 0              , part_of_10):
        return
    if not mergeTraffic(mergedValidFiles, foregroundValidFiles, dir_background, part_of_10 + 1 , part_of_10*2):
        return
    if not mergeTraffic(mergedTrainFiles, foregroundTrainFiles, dir_background, part_of_10*2 + 1, int(df_len)):
        return


    print("Succeeded in creating the merged traffic set")

if __name__=="__main__":
    main()