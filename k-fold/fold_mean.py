#!/usr/bin/env python3

import os
import pandas as pd

'''
merge the 10 fold, so it can be showed as one graph
'''
def main():
    PATH_INPUT = "wf-result/undef"
    PATH_OUTPUT = "wf-result/undef/combined.csv"
    os.system("rm " + PATH_OUTPUT)
   
    df_list = []
    for csv_file in os.listdir(PATH_INPUT):
        df_list.append(pd.read_csv(PATH_INPUT + "/" + csv_file))

    df_output = df_list[0]
    df_len = df_list.len()
    df_list.pop(0)


    # add all accuracy
    for df in df_list:
        for index, row in df.iterrows():
            df_output["accuracy"].loc[index] += row["accuracy"]
        
    # mean for each value
    for index, row in df_output.iterrows():
        row["accuracy"] = row["accuracy"] / df_len

    # save result
    df_output.to_csv(PATH_OUTPUT, index = False)

# run main 
if __name__=="__main__":
    main()