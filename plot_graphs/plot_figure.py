import sys
import pandas as pd

def plot_figure(files2plot, subtitle ,x_label, y_label, sup_title = "", result_path  = "fig/" ):
    '''
    Plot a figure of the provided subplots (3 or 4)
    Args:
        files       - Required : path to files to plot                    (List[str])
        sub_title   - Required : list fo titles for each subgraph (List[str])
        x_label     - Required : label for the x axis             (str)
        y_label     - Required : label for the y axis             (str)
        sup_title   - Optional : title for the figure             (str)
        result_path - Optional : where to store the figure        (str)
    '''

    # Extract all csv files that should be plotted in a graph
    datasets = []
    for csv_file in files2plot:
        df = pd.read_csv(csv_file, usecols = ["th", "accuracy"], index_col = None)
        datasets.append(df)

    if len(datasets) == 4:
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        fig.subplots_adjust(top=0.8)

        for i in range(4):
            axes[(i%2),(i%1)].plot(datasets[i])
            axes[(i%2),(i%1)].set_title(subtitle[i])
            axes[(i%2),(i%1)].set_ylabel(y_label)
            axes[(i%2),(i%1)].set_xlabel(x_label)

        # save result and clear the plotting
        fig.suptitle(title)
        fig.tight_layout()
        fig.savefig(f"{result_path}{title}.png")
        plt.close(fig)

    elif len(datasets) == 3:
        fig, axes = plt.subplots(3, 1, figsize=(10, 10))
        fig.subplots_adjust(top=0.8)

        for i in range(3):
            axes[i].plot(datasets[i])
            axes[i].set_title(subtitle[i])
            axes[i].set_ylabel(y_label)
            axes[i].set_xlabel(x_label)

        # save result and clear the plotting
        fig.suptitle(title)
        fig.tight_layout()
        fig.savefig(f"{result_path}{title}.png")
        plt.close(fig)

    else:
        print("ERROR: One must use 3 or 4 files per figure")
        sys.exit()

    return