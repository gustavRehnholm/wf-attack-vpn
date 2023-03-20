#!/usr/bin/python3

'''
This program merges the web traffic with noise, so it can be used to test WF attacks

If the program runs out of primary memory during its run time, test to make the variable chunk smaller

python wf-attack-vpn/generate_merged_dataset/main.py
'''

import pandas as pd
import os
from merge_datasets_offset    import mergeDatasetNoiseOffset
from merge_dataset_rnd        import mergeDatasetNoiseRnd
from merge_dataset_divide     import mergeDatasetNoiseDivide
from merge_dataset_divide_rnd import mergeDatasetNoiseDivideRnd

'''
Input:
    dir_foreground: path to the directory that has the foreground that the background should be merged into
    dir_merged: path to the directory where the merged result will be stored in
    dir_background: path to the directory where the background traffic is
    background_amount: if one wish to use 1/x amount of the available background traffic
    offset: if one uses offset or not
    random: if one should go through the background traffic in order (false) or random (true)
    divide: if the background data should be divided among the training, testing and validation
'''
def generateMergedTraffic(dir_foreground, dir_merged, dir_background, background_amount = 1, offset = True, random = True, divide = False):

    FOLD0_CSV = dir_foreground + "/fold-0.csv"
    key    = "df"

    if offset:
        offset_test = 0.3
        offset_valid = 0.6
    else:
        offset_test = 0
        offset_valid = 0
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
    df = pd.read_csv(FOLD0_CSV)
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

    if not divide:
        if random:
            if not mergeDatasetNoiseRnd(mergedTestFiles, foregroundTestFiles, dir_background, offset_test, chunk, background_amount = background_amount):
                return
            if not mergeDatasetNoiseRnd(mergedValidFiles, foregroundValidFiles, dir_background, offset_valid, chunk, background_amount = background_amount):
                return
            if not  mergeDatasetNoiseRnd(mergedTrainFiles, foregroundTrainFiles, dir_background, offset_train, chunk, background_amount = background_amount):
                return
        else:
            if not mergeDatasetNoiseOffset(mergedTestFiles, foregroundTestFiles, dir_background, offset_test, chunk, background_amount = background_amount):
                return
            if not mergeDatasetNoiseOffset(mergedValidFiles, foregroundValidFiles, dir_background, offset_valid, chunk, background_amount = background_amount):
                return
            if not mergeDatasetNoiseOffset(mergedTrainFiles, foregroundTrainFiles, dir_background, offset_train, chunk, background_amount = background_amount):
                return
    else:
        # get size of the background traffic
        store = pd.HDFStore(dir_background)
        df_len = store.get_storer(key).nrows
        store.close()

        df_len = round(df_len / background_amount)
        part_of_10 = round(df_len/10)

        print("Size of the background")
        print(df_len)

        if random:
            if not mergeDatasetNoiseDivideRnd(mergedTestFiles, foregroundTestFiles, dir_background, 0              , part_of_10  , chunk, background_amount = background_amount):
                return
            if not mergeDatasetNoiseDivideRnd(mergedValidFiles, foregroundValidFiles, dir_background, part_of_10 + 1 , part_of_10*2, chunk, background_amount = background_amount):
                return
            if not mergeDatasetNoiseDivideRnd(mergedTrainFiles, foregroundTrainFiles, dir_background, part_of_10*2 + 1, int(df_len), chunk, background_amount = background_amount):
                return
        else:
            if not mergeDatasetNoiseDivide(mergedTestFiles,  foregroundTestFiles,  dir_background, 0              , part_of_10  , chunk, background_amount = background_amount):
                return
            if not mergeDatasetNoiseDivide(mergedValidFiles, foregroundValidFiles, dir_background, part_of_10 + 1 , part_of_10*2, chunk, background_amount = background_amount):
                return
            if not mergeDatasetNoiseDivide(mergedTrainFiles, foregroundTrainFiles, dir_background, part_of_10*2 + 1, int(df_len), chunk, background_amount = background_amount):
                return


    print("Succeeded in creating the merged traffic set")

if __name__=="__main__":
    main()