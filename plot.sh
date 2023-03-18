#!/bin/bash
# Plot all the result graphs

# input: {title} {csv file 1} {csv file 2} ...

# DF size, constant and tiktok
python3 wf-attack-vpn/plotter/plot_df.py twitch_4h  wf-result/twitch_small_offset_30_60_0/twitch_constant.csv wf-result/twitch_small_offset_30_60_0/twitch_tiktok.csv

python3 wf-attack-vpn/plotter/plot_df.py twitch_whole  wf-result/twitch_offset_30_60_0/twitch_default.csv wf-result/twitch_offset_30_60_0/twitch_constant.csv wf-result/twitch_offset_30_60_0/twitch_tiktok.csv

#merged_traffic/twitch_smallest_offset_30_60_0

python3 wf-attack-vpn/plotter/plot_df.py twitch_2h  wf-result/twitch_smallest_offset_30_60_0/twitch_default.csv wf-result/twitch_smallest_offset_30_60_0/twitch_constant.csv wf-result/twitch_smallest_offset_30_60_0/twitch_tiktok.csv
