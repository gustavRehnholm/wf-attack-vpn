#!/usr/bin/env python3

import os
import pandas as pd

'''
merge the 10 fold, so it can be showed as one graph
'''
def main():
    PATH_INPUT = "merged_traffic/undef"
    PATH_OUTPUT = "merged_traffic/undef/combined.csv"
    os.system("rm " + PATH_OUTPUT)
   
    df_list = []
    for csv_file in os.listdir(PATH_INPUT):
        df_list.append(pd.read_csv(csv_file))

    df = pd.concat(df_list)
    foo = df.groupby(level=1).mean()
    foo.head()

    foo.to_csv(PATH_OUTPUT, index = False)

# run main 
if __name__=="__main__":
    main()