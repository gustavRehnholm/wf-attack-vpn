#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# navie approach
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset wf_result/twitch/twitch_no_offset wf-result/twitch/twitch_no_offset

# offset
python wf-attack-vpn/plotter/plot_all.py twitch_offset wf_result/twitch/twitch_offset wf-result/twitch/twitch_offset

# rnd chunks
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset wf_result/twitch/twitch_rnd_no_offset wf-result/twitch/twitch_rnd_no_offset