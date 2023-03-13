#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

If the program runs out of primary memory during its run time, test to make the variable chunk smaller

Input (sys.argv):
[1] : chunk size
[2] : offsett for the test files
[3] : offset for the valid files
[4] : offset for the train files
[5] : directory for the foreground traffic to use
[6] : directory for the merged traffic to use
[7] : directory for the background traffic file to use

python wf-attack-vpn/generate_merged_dataset/main.py
'''

import pandas as pd
import os
from merge_dataset_noise import mergeDatasetNoise

def main():

    # TODO: gather from the user
    DIR_FOREGROUND = "foreground_traffic"
    DIR_MERGED     = "merged_traffic/twitch_small_offset_30_60_0"

    DIR_BACKGROUND = "background_traffic"
    FILE_BACKBROUND = "twitch.h5"
    PATH_BACKGROUND = DIR_BACKGROUND + "/" + FILE_BACKBROUND

    FOLD0_CSV = DIR_FOREGROUND + "/fold-0.csv"


    key    = "df"
    offset_test = 0.3
    offset_valid = 0.6
    offset_train = 0
    # how many rows of background the computer will have in the primary memory at a time
    chunk = 10000

    # list of what each file should be used for
    foregroundTrainFiles = []
    foregroundValidFiles = []
    foregroundTestFiles  = []
    mergedTrainFiles = []
    mergedValidFiles = []
    mergedTestFiles  = []


    print("Start the test of the merging of foreground and background traffic")

    # clean the previous result
    os.system("rm -f -r " + DIR_MERGED)
    os.system("mkdir " + DIR_MERGED)


    # The naming structure between the foreground and the merged should be the same
    for (dirpath, dirnames, filenames) in os.walk(DIR_FOREGROUND, topdown=True):
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
            foregroundTrainFiles.append(os.path.join(DIR_FOREGROUND, "client", dfFiles['log'][x]))

        elif(dfFiles['is_valid'][x] == True): 
            mergedValidFiles.append(os.path.join(DIR_MERGED, dfFiles['log'][x]))
            foregroundValidFiles.append(os.path.join(DIR_FOREGROUND, "client", dfFiles['log'][x]))

        elif(dfFiles['is_test'][x] == True): 
            mergedTestFiles.append(os.path.join(DIR_MERGED, dfFiles['log'][x]))
            foregroundTestFiles.append(os.path.join(DIR_FOREGROUND, "client", dfFiles['log'][x]))

        else:
            print("ERROR: the file " + dfFiles['log'][x] + "does not have a determined usage")
            print("Aborting program")
            return



    result = mergeDatasetNoise(mergedTestFiles, foregroundTestFiles, PATH_BACKGROUND, offset_test, chunk)
    if result is False:
        return
    result = mergeDatasetNoise(mergedValidFiles, foregroundValidFiles, PATH_BACKGROUND, offset_valid, chunk)
    if result is False:
        return
    result = mergeDatasetNoise(mergedTrainFiles, foregroundTrainFiles, PATH_BACKGROUND, offset_train, chunk)
    if result is False:
        return

    print("Succeeded in creating the merged traffic set")

if __name__=="__main__":
    main()