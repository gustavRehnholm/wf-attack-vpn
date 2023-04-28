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

import argparse
import os
import sys
from plot_df import plotDf

ap = argparse.ArgumentParser()
ap.add_argument("--title" , required = True, default = "", type = str, help = "title of the graph")
ap.add_argument("--input" , required = True, default = "", type = str, help = "root folder of the DF result")
ap.add_argument("--output", required = True, default = "", type = str, help = "path where the graph will be stored")
args = vars(ap.parse_args())


def main():
    print("Creates a graph from all csv files provided in a directory")

    labels = []
    title  = args['title']
    input  = args['input']
    output = args['output']
    
    # path to each size of 
    csv_dir    = os.listdir(input)
    files2plot = []

    for file in csv_dir:
        files2plot.append(input + "/" + file)
        labels.append(file.split(".")[0])

    # create path for the result
    splitted_result_path = os.path.dirname(output)
    os.system("mkdir " + splitted_result_path)
    os.system("mkdir " + output)

    result = output + "/"

    plotDf(title = title, list_of_csv = files2plot, labels = labels, result_path = result)

# run main 
if __name__=="__main__":
    main()