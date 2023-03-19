#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# navie approach
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset_2600h wf-result/twitch/twitch_no_offset/twitch_no_offset_2600h wf-result/twitch/twitch_no_offset/twitch_no_offset_2600h
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset_5h    wf-result/twitch/twitch_no_offset/twitch_no_offset_5h    wf-result/twitch/twitch_no_offset/twitch_no_offset_5h
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset_2_5h  wf-result/twitch/twitch_no_offset/twitch_no_offset_2_5h  wf-result/twitch/twitch_no_offset/twitch_no_offset_2_5h

# offset
#python wf-attack-vpn/plotter/plot_all.py twitch_offset wf-result/twitch/twitch_offset wf-result/twitch/twitch_offset

# rnd chunks
#python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset wf-result/twitch/twitch_rnd_no_offset wf-result/twitch/twitch_rnd_no_offset