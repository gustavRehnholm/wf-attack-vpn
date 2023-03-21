#!/bin/bash

# plot the test for 100 sample size

# ./wf-attack-vpn/plotter/plot_100.sh

# rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_100_2600h wf-result/twitch_rnd_no_offset_100/twitch_rnd_no_offset_2600h fig/twitch_rnd_no_offset_100
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_100_5h    wf-result/twitch_rnd_no_offset_100/twitch_rnd_no_offset_5h    fig/twitch_rnd_no_offset_100
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_100_2_5h  wf-result/twitch_rnd_no_offset_100/twitch_rnd_no_offset_2_5h  fig/twitch_rnd_no_offset_100

# rnd with offset
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_100_2600h wf-result/twitch_rnd_offset_100/twitch_rnd_offset_2600h fig/twitch_rnd_offset_100
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_100_5h    wf-result/twitch_rnd_offset_100/twitch_rnd_offset_5h    fig/twitch_rnd_offset_100
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_100_2_5h  wf-result/twitch_rnd_offset_100/twitch_rnd_offset_2_5h  fig/twitch_rnd_offset_100

# div ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_100_2600h wf-result/twitch_div_ittr_100/twitch_div_ittr_2600h fig/twitch_div_ittr_100
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_100_5h    wf-result/twitch_div_ittr_100/twitch_div_ittr_5h    fig/twitch_div_ittr_100
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_100_2_5h  wf-result/twitch_div_ittr_100/twitch_div_ittr_2_5h  fig/twitch_div_ittr_100

# div rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_2600h wf-result/twitch_div_rnd_100/twitch_div_rnd_2600h fig/twitch_div_rnd_100
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_5h    wf-result/twitch_div_rnd_100/twitch_div_rnd_5h    fig/twitch_div_rnd_100
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_2_5h  wf-result/twitch_div_rnd_100/twitch_div_rnd_2_5h  fig/twitch_div_rnd_100