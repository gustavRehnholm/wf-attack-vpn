#!/usr/bin/env python3

import os
import pandas as pd
import sys

'''
merge the 10 fold, so it can be showed as one graph
'''
def main():
    PATH_INPUT  = sys.argv[1]
    PATH_OUTPUT = sys.argv[2]
    os.system("rm " + PATH_OUTPUT)
   
    df_list = []
    for csv_file in os.listdir(PATH_INPUT):
        df_list.append(pd.read_csv(PATH_INPUT + "/" + csv_file))

    df_output = df_list[0]
    df_len = len(df_list)

    acc_list = [0] * len(df_output.index)

    # add all accuracy
    for df in df_list:
        for index, row in df.iterrows():
            acc_list[index] += row["accuracy"]
        
    # mean for each value
    for index, row in df_output.iterrows():
        row["accuracy"] = acc_list[index] / df_len

    # save result
    df_output.to_csv(PATH_OUTPUT, index = False)

# run main 
if __name__=="__main__":
    main()