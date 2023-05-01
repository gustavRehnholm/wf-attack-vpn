import sys
import os
import pandas as pd

def plot_figure(figure_dir, subtitle ,x_label, y_label, sup_title = "", result_path  = "fig/" ):
    '''
    Plot a figure of the provided subplots (3 or 4)
    Args:
        figure_dir  - Required : path to files to plot                    (List[str])
        sub_title   - Required : list fo titles for each subgraph (List[str])
        x_label     - Required : label for the x axis             (str)
        y_label     - Required : label for the y axis             (str)
        sup_title   - Optional : title for the figure             (str)
        result_path - Optional : where to store the figure        (str)
    '''

    # Extract all csv files that should be plotted in a graph
    subplots_paths = os.listdir(figure_dir)
    nr_subplots    = len(subplots_paths)
    datasets_per_subplot = []

    for subplot_dir in subplots_paths:
        path = f"{figure_dir}/{subplot_dir}"
        datasets = []
        for csv_file in path:
            df = pd.read_csv(csv_file, usecols = ["th", "accuracy"], index_col = None)
            datasets.append(df)

        datasets_per_subplot.append(datasets)

    # 4 subplots per figure
    if nr_subplots == 4:
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        fig.subplots_adjust(top=0.8)

        # plot every subplot
        for index_subplot in range(4):
            # every line for the subplot
            for index_line in range(len(datasets_per_subplot[index_subplot])):   
                axes[(index_subplot%2),(index_subplot%1)].plot(datasets_per_subplot[index_subplot][index_line])
            axes[(index_subplot%2),(index_subplot%1)].set_title(subtitle[index_subplot])
            axes[(index_subplot%2),(index_subplot%1)].set_ylabel(y_label)
            axes[(index_subplot%2),(index_subplot%1)].set_xlabel(x_label)

        # save result and clear the plotting
        fig.suptitle(title)
        fig.tight_layout()
        fig.savefig(f"{result_path}{title}.png")
        plt.close(fig)

    # 3 subplots per figure
    elif nr_subplots == 3:
        fig, axes = plt.subplots(3, 1, figsize=(10, 10))
        fig.subplots_adjust(top=0.8)

        for index_subplot in range(3):
            for index_line in range(len(datasets_per_subplot[index_subplot])):   
                axes[index_subplot].plot(datasets_per_subplot[index_subplot][index_line])
            axes[index_subplot].set_title(subtitle[index_subplot])
            axes[index_subplot].set_ylabel(y_label)
            axes[index_subplot].set_xlabel(x_label)

        # save result and clear the plotting
        fig.suptitle(title)
        fig.tight_layout()
        fig.savefig(f"{result_path}{title}.png")
        plt.close(fig)

    else:
        print("ERROR: One must use 3 or 4 subfigures per figure")
        sys.exit()

    return