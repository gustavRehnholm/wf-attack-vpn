

def plot_figure(files2plot, subtitle ,x_label, y_label, sup_title = "", result_path  = "fig/" ):
    '''
    Plot a figure of the provided subplots (3 or 4)
    Args:
        files       - Required : files to plot                    (List[str])
        sub_title   - Required : list fo titles for each subgraph (List[str])
        x_label     - Required : label for the x axis             (str)
        y_label     - Required : label for the y axis             (str)
        sup_title   - Optional : title for the figure             (str)
        result_path - Optional : where to store the figure        (str)
    '''

    if len(files2plot) == 4:
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        fig.subplots_adjust(top=0.8)

        for i in range(4):
            axes[(i%2),(i%1)].plot(files2plot[i])
            axes[(i%2),(i%1)].set_title(subtitle[i])
            axes[(i%2),(i%1)].set_ylabel(y_label)
            axes[(i%2),(i%1)].set_xlabel(x_label)

        # save result and clear the plotting
        fig.suptitle(title)
        fig.tight_layout()
        fig.savefig(f"{result_path}{title}.png")
        plt.close(fig)

    elif len(files2plot) == 3:
        fig, axes = plt.subplots(3, 1, figsize=(10, 10))
        fig.subplots_adjust(top=0.8)

        for i in range(3):
            axes[i].plot(files2plot[i])
            axes[i].set_title(subtitle[i])
            axes[i].set_ylabel(y_label)
            axes[i].set_xlabel(x_label)

        # save result and clear the plotting
        fig.suptitle(title)
        fig.tight_layout()
        fig.savefig(f"{result_path}{title}.png")
        plt.close(fig)

    return