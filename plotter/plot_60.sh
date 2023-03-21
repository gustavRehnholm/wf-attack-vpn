#!/bin/bash

# plot the test for 60 sample size

# ./wf-attack-vpn/plotter/plot_60.sh

# rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_60_2600h wf-result/twitch_rnd_no_offset_60/twitch_rnd_no_offset_2600h fig/twitch_rnd_no_offset_60
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_60_5h    wf-result/twitch_rnd_no_offset_60/twitch_rnd_no_offset_5h    fig/twitch_rnd_no_offset_60
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_60_2_5h  wf-result/twitch_rnd_no_offset_60/twitch_rnd_no_offset_2_5h  fig/twitch_rnd_no_offset_60

# rnd with offset
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_60_2600h wf-result/twitch_rnd_offset_60/twitch_rnd_offset_2600h fig/twitch_rnd_offset_60
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_60_5h    wf-result/twitch_rnd_offset_60/twitch_rnd_offset_5h    fig/twitch_rnd_offset_60
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_60_2_5h  wf-result/twitch_rnd_offset_60/twitch_rnd_offset_2_5h  fig/twitch_rnd_offset_60

# div ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_60_2600h wf-result/twitch_div_ittr_60/twitch_div_ittr_2600h fig/twitch_div_ittr_60
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_60_5h    wf-result/twitch_div_ittr_60/twitch_div_ittr_5h    fig/twitch_div_ittr_60
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_60_2_5h  wf-result/twitch_div_ittr_60/twitch_div_ittr_2_5h  fig/twitch_div_ittr_60

# div rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_60_2600h wf-result/twitch_div_rnd_60/twitch_div_rnd_2600h fig/twitch_div_rnd_60
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_60_5h    wf-result/twitch_div_rnd_60/twitch_div_rnd_5h    fig/twitch_div_rnd_60
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_60_2_5h  wf-result/twitch_div_rnd_60/twitch_div_rnd_2_5h  fig/twitch_div_rnd_60