#!/usr/bin/env python3

'''
To plot the result from the WF training
input: {title} {csv file 1} {csv file 2} ...

./wf-attack-vpn/plotter/plot.sh
or
python wf-attack-vpn/plotter/plot_all.py
'''

import os
import sys
from plot_df import plotDf

'''
sys.argv[1] : title
sys.argv[2] : path to dir
'''
def main():

    print("Creates a graph from all csv files provided in a directory")

    labels = ["default", "constant", "tiktok"]

    
    title = sys.argv[1]
    path = sys.argv[2]
    
    csv_files = os.listdir(path)
    

    plotDf(title = title, list_of_csv = csv_files, labels = labels)


# run main 
if __name__=="__main__":
    main()