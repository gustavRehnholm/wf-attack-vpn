#!/usr/bin/env python3

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plotDf(title = "untitled", list_of_csv = [], labels = [], result_path = "fig/"):
    '''
    Plot graph of the provided WF results
    Args:
        title       - Optional : Title of the graph
        list_of_csv - Required : The WF result to plot the graph for
        labels      - Optional : labels of the plotted lines
        result_path - Optional : Where to store the generated graph figure
    '''

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

    # plot all lines for the graph
    for j in range(0, len(datasets)):
        ax = sns.pointplot(data = datasets[j][["th", "accuracy"]], x ="th", y="accuracy", color = colors[j], label = labels[j])

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