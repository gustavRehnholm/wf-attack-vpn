#!/usr/bin/env python3

'''
To plot the result from the WF training
input: {title} {csv file 1} {csv file 2} ...

TODO: Stop program if it can not create the result dir
TODO: check that the input paths exists

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
sys.argv[3] : path for result
'''
def main():
    print("Creates a graph from all csv files provided in a directory")

    labels = []
    title  = sys.argv[1]
    path   = sys.argv[2]
    
    # path to each size of 
    csv_dir    = os.listdir(path)
    files2plot = []

    for file in csv_dir:
        files2plot.append(path + "/" + file)
        labels.append(file.split(".")[0])

    # create path for the result
    splitted_result_path = os.path.dirname(sys.argv[3])
    os.system("mkdir " + splitted_result_path)
    os.system("mkdir " + sys.argv[3])

    result = sys.argv[3] + "/"

    plotDf(title = title, list_of_csv = files2plot, labels = labels, result_path = result)

# run main 
if __name__=="__main__":
    main()