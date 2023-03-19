#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# navie approach
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset merged_traffic/twitch/twitch_no_offset wf-result/twitch/twitch_no_offset

# offset
python wf-attack-vpn/plotter/plot_all.py twitch_offset merged_traffic/twitch/twitch_offset wf-result/twitch/twitch_offset

# rnd chunks
python wf-attack-vpn/plotter/plot_all.py twitch_rnd merged_traffic/twitch/twitch_rnd wf-result/twitch/twitch_rnd