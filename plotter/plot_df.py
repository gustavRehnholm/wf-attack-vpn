#!/usr/bin/env python3

'''
To plot the result from the WF training

python /rds-collect2/plotter/plot_all.py
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd
import sys
import os

'''

'''
def plotDf(title = "untitled", list_of_csv = [], labels = [], result_path = "fig/"):

    colors = sns.color_palette(n_colors = len(list_of_csv))
    
    # Extract all csv files that should be plotted in a graph
    datasets = []
    for csv_file in list_of_csv:
        df = pd.read_csv(csv_file, usecols = ["th", "accuracy"], index_col = None)
        datasets.append(df)

    # end program if data is unsuable
    if len(datasets) <= 0:
        print("ERROR: there is no inputted files")
        print("Aborting program")
        return
    elif len(datasets) > len(colors):
        print("ERROR: there are more lines to plot than colors, add more colors in the colors list")
        print("There is ", len(datasets), " lines to show in the graphs")
        print("Aborting program")
        return
    elif len(datasets) > len(labels):
        print("ERROR: there are more lines to plot than labels, add more labels in the labels list")
        print("There is ", len(datasets), " lines to show in the graphs")
        print("Aborting program")
        

    # plot all lines for the graph
    for j in range(0, len(datasets)):
        ax = sns.pointplot(data = datasets[j][["th", "accuracy"]], x ="th", y="accuracy", color = colors[j], label = labels[j])

    #x_ticks = [0.1, 0.5, 0.7, 0.9]
    #labels_x = ["0.1", "0.5", "0.7", "0.9"]
    #plt.xticks(ticks = x_ticks, rotation ='horizontal')

    #ax.set_xticks(range(0, len(labels_x)))
    #ax.set_xticklabels(labels_x)

    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom = 0.15)

    plt.legend()
    plt.title(title)

    fig = plt.gcf()
    os.system("rm " + str(result_path + title) + ".png")
    fig.savefig(result_path + title)

    plt.show()


# run main 
if __name__=="__main__":
    main()