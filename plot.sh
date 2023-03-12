#!/bin/bash
# Plot all the result graphs

# input: {title} {csv file 1} {csv file 2} ...

# DF size, constant and tiktok
python3 wf-attack-vpn/plotter/plot_df.py whole_twitch wf-result/twitch_default.csv wf-result/twitch_constant.csv wf-result/twitch_tiktok.csv