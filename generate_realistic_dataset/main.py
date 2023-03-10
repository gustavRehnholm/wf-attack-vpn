#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

python wf-attack-vpn/generate_realistic_dataset/main.py
'''

import pandas as pd
from os import walk
from merge_dataset_noise import mergeDatasetNoise

def main():

    # TODO: gather from the user
    DIR_FOREGROUND = "dataset"
    DIR_MERGED     = "merged_traffic"

    DIR_BACKGROUND = "background_traffic"
    FILE_BACKBROUND = "twitch.h5"
    PATH_BACKGROUND = DIR_BACKGROUND + "/" + FILE_BACKBROUND


    key    = "df"
    offset = 0

    # list of what each file should be used for
    foregroundTrainFiles = []
    foregroundValidFiles = []
    foregroundTestFiles  = []
    mergedTrainFiles = []
    mergedValidFiles = []
    mergedTestFiles  = []


    print("Start the test of the merging of foreground and background traffic")


    # The naming structure between the foreground and the merged should be the same
    for (dirpath, dirnames, filenames) in walk(DIR_FOREGROUND, topdown=True):
        for dirs in dirnames:
            try: 
                os.mkdir(os.path.join(DIR_MERGED, dirs))
            except: 
                print("File and directory exists!") 


    # dataframe representation of what each foreground file should be used for
    df = pd.read_csv(FOLD0_CSV)
    FOLD_DF_ATTR = ['log', 'is_train', 'is_valid', 'is_test']
    dfFiles = df[FOLD_DF_ATTR]

    # For every log file in the web traffic, make sure that there is an correlating log file to store the parsed result
    for x in range(0, len(dfFiles['log'])):
        if(dfFiles['is_train'][x] == True): 
            mergedTrainFiles.append(os.path.join(DIR_MERGED, dfFiles['log'][x]))
            foregroundTrainFiles.append(os.path.join(DIR_FOREGROUND,"client", dfFiles['log'][x]))
        elif(dfFiles['is_valid'][x] == True): 
            mergedValidFiles.append(os.path.join(DIR_MERGED, dfFiles['log'][x]))
            foregroundValidFiles.append(os.path.join(DIR_FOREGROUND,"client", dfFiles['log'][x]))
        elif(dfFiles['is_test'][x] == True): 
            mergedTestFiles.append(os.path.join(DIR_MERGED, dfFiles['log'][x]))
            foregroundTestFiles.append(os.path.join(DIR_FOREGROUND,"client", dfFiles['log'][x]))
        else:
            print("ERROR: the file " + dfFiles['log'][x] + "does not have a determined usage")
            print("Aborting program")
            return



    result = mergeDatasetNoise(mergedTestFiles, foregroundTestFiles, PATH_BACKGROUND, offsets)
    if result is False:
        return
    result = mergeDatasetNoise(mergedValidFiles, foregroundValidFiles, PATH_BACKGROUND, offsets)
    if result is False:
        return
    result = mergeDatasetNoise(mergedTrainFiles, foregroundTrainFiles, PATH_BACKGROUND, offsets)
    if result is False:
        return

    print("Succeeded in creating the merged traffic set")

if __name__=="__main__":
    main()