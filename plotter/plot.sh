#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# undefended plot
python wf-attack-vpn/plotter/plot_all.py --title twitch_undef_100 --input wf-result/undef_100/10-fold --output fig/undef

# replicated twitch dataset
python wf-attack-vpn/plotter/plot_all.py --title twitch_old_og  --input wf-result/twitch_old/old_twitch_og  --output fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py --title twitch_old_20  --input wf-result/twitch_old/old_twitch_20  --output fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py --title twitch_old_100 --input wf-result/twitch_old/old_twitch_100 --output fig/twitch_old

# rnd, sample 100
#python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_100h wf-result/twitch_rnd_100/twitch_rnd_100h         fig/twitch_rnd
#python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_2h   wf-result/twitch_rnd_100/twitch_div_rnd_first_2h fig/twitch_rnd
#python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_2h   wf-result/twitch_rnd_100/twitch_div_rnd_last_2h  fig/twitch_rnd

# Divided, randomized, sample 100 (the largest part of the Twitch dataset)
python wf-attack-vpn/plotter/plot_all.py --title twitch_div_rnd_100h      --input wf-result/twitch_div_rnd/twitch_div_rnd_100h      --output fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py --title twitch_div_rnd_first_2h  --input wf-result/twitch_div_rnd/twitch_div_rnd_first_2h  --output fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py --title twitch_div_rnd_last_2h   --input wf-result/twitch_div_rnd/twitch_div_rnd_last_2h   --output fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py --title twitch_div_rnd_middle_2h --input wf-result/twitch_div_rnd/twitch_div_rnd_middle_2h --output fig/twitch_div_rnd

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
python wf-attack-vpn/plotter/plot_all.py --title compare_default  --input wf-result/compare_default  --output fig/compare
python wf-attack-vpn/plotter/plot_all.py --title compare_constant --input wf-result/compare_constant --output fig/compare
python wf-attack-vpn/plotter/plot_all.py --title compare_tiktok   --input wf-result/compare_tiktok   --output fig/compare