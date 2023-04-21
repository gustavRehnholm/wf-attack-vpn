#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# undefended plot
python wf-attack-vpn/plotter/plot_all.py twitch_undef_100 wf-result/undef_100/10-fold fig/undef

# replicated twitch dataset
python wf-attack-vpn/plotter/plot_all.py twitch_old_og  wf-result/twitch_old/old_twitch_og  fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py twitch_old_20  wf-result/twitch_old/old_twitch_20  fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py twitch_old_100 wf-result/twitch_old/old_twitch_100 fig/twitch_old

# rnd, sample 100
#python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_100h wf-result/twitch_rnd_100/twitch_rnd_100h         fig/twitch_rnd
#python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_2h   wf-result/twitch_rnd_100/twitch_div_rnd_first_2h fig/twitch_rnd
#python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_2h   wf-result/twitch_rnd_100/twitch_div_rnd_last_2h  fig/twitch_rnd

# Divided, randomized, sample 100 (the largest part of the Twitch dataset)
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100h       wf-result/twitch_div_rnd/twitch_div_rnd_100h      fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_first_2h   wf-result/twitch_div_rnd/twitch_div_rnd_first_2h  fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_last_2h    wf-result/twitch_div_rnd/twitch_div_rnd_last_2h   fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_middle_2h  wf-result/twitch_div_rnd/twitch_div_rnd_middle_2h fig/twitch_div_rnd

# cp files for the comparison

# 100 default
cp wf-result/undef_100/combined/combined.csv                    wf-result/compare_default/undef.csv
cp wf-result/twitch_old/old_twitch_100/default.csv              wf-result/compare_default/twitch.csv
cp wf-result/twitch_div_rnd/twitch_div_rnd_last_2h/default.csv  wf-result/compare_default/rnd_last.csv
cp wf-result/twitch_div_rnd/twitch_div_rnd_first_2h/default.csv wf-result/compare_default/rnd_first.csv

# 100 constant
cp wf-result/undef_100/combined/combined.csv                     wf-result/compare_constant/undef.csv
cp wf-result/twitch_old/old_twitch_100/constant.csv              wf-result/compare_constant/twitch.csv
cp wf-result/twitch_div_rnd/twitch_div_rnd_last_2h/constant.csv  wf-result/compare_constant/rnd_last.csv
cp wf-result/twitch_div_rnd/twitch_div_rnd_first_2h/constant.csv wf-result/compare_constant/rnd_first.csv

# 100 Tik-Tok
cp wf-result/undef_100/combined/combined.csv                   wf-result/compare_tiktok/undef.csv
cp wf-result/twitch_old/old_twitch_100/tiktok.csv              wf-result/compare_tiktok/twitch.csv
cp wf-result/twitch_div_rnd/twitch_div_rnd_last_2h/tiktok.csv  wf-result/compare_tiktok/rnd_last.csv
cp wf-result/twitch_div_rnd/twitch_div_rnd_first_2h/tiktok.csv wf-result/compare_tiktok/rnd_first.csv

# The final comparison graph
python wf-attack-vpn/plotter/plot_all.py compare_default   wf-result/compare_default   fig/compare
python wf-attack-vpn/plotter/plot_all.py compare_constant  wf-result/compare_constant  fig/compare
python wf-attack-vpn/plotter/plot_all.py compare_tiktok    wf-result/compare_tiktok    fig/compare