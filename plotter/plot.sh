#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# navie approach
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset_2600h wf-result/twitch/twitch_no_offset/twitch_no_offset_2600h fig/twitch_no_offset
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset_5h    wf-result/twitch/twitch_no_offset/twitch_no_offset_5h    fig/twitch_no_offset
python wf-attack-vpn/plotter/plot_all.py twitch_no_offset_2_5h  wf-result/twitch/twitch_no_offset/twitch_no_offset_2_5h  fig/twitch_no_offset

# offset
python wf-attack-vpn/plotter/plot_all.py twitch_offset_2600h wf-result/twitch/twitch_offset/twitch_offset_2600h fig/twitch_offset
python wf-attack-vpn/plotter/plot_all.py twitch_offset_5h    wf-result/twitch/twitch_offset/twitch_offset_5h    fig/twitch_offset
python wf-attack-vpn/plotter/plot_all.py twitch_offset_2_5h  wf-result/twitch/twitch_offset/twitch_offset_2_5h  fig/twitch_offset

# rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_2600h wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h fig/twitch_rnd_no_offset
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_5h    wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    fig/twitch_rnd_no_offset
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_no_offset_2_5h  wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  fig/twitch_rnd_no_offset

# rnd with offset
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_2600h wf-result/twitch/twitch_rnd_offset/twitch_rnd_offset_2600h fig/twitch_rnd_offset
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_5h    wf-result/twitch/twitch_rnd_offset/twitch_rnd_offset_5h    fig/twitch_rnd_offset
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_offset_2_5h  wf-result/twitch/twitch_rnd_offset/twitch_rnd_offset_2_5h  fig/twitch_rnd_offset

# div ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_2600h wf-result/twitch/twitch_div_ittr/twitch_div_ittr_2600h fig/twitch_div_ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_5h    wf-result/twitch/twitch_div_ittr/twitch_div_ittr_5h    fig/twitch_div_ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_2_5h  wf-result/twitch/twitch_div_ittr/twitch_div_ittr_2_5h  fig/twitch_div_ittr

# div rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_2600h wf-result/twitch/twitch_div_rnd/twitch_div_rnd_2600h fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_5h    wf-result/twitch/twitch_div_rnd/twitch_div_rnd_5h    fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_2_5h  wf-result/twitch/twitch_div_rnd/twitch_div_rnd_2_5h  fig/twitch_div_rnd