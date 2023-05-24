# Plotting WF results

This folder contains the scripts to plot the result, and in the folder scripts, to run a longer test

## bash scripts
the folder scripts contains all bash scripts used to generate the result needed.

## programs to run
The root folder contains python scripts to generate the graphs.

### plot_all.py
This plots multiple figures from the provided root folder, as long as it follows the following structure:
input/figures/subplots/lines

### plot_figure.py
This plots one figure with subplots, by providing the root folder with the structure:
input/subplots/lines

### result_print.py
This restructure the result data, so that one goes from one graph per fold, to one graph per mode

### worst_case_print.py
Generate the worst case scenario with the MIT dataset. Takes a long time and required roughly 300GB disk space for 10,000 packet per file, and half of that for 5,000 packets per file.