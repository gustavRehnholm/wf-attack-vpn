#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# undefended plot
python wf-attack-vpn/plotter/plot_all.py twitch_undef_100 wf-result/undef_100/10-fold fig/undef
python wf-attack-vpn/plotter/plot_all.py twitch_undef_20  wf-result/undef_20/10-fold  fig/undef

# replicated twitch dataset
python wf-attack-vpn/plotter/plot_all.py twitch_old_og  wf-result/twitch_old/old_twitch_og  fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py twitch_old_20  wf-result/twitch_old/old_twitch_20  fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py twitch_old_100 wf-result/twitch_old/old_twitch_100 fig/twitch_old

# offset. sample 20
#python wf-attack-vpn/plotter/plot_all.py twitch_offset_2600h wf-result/twitch_offset/twitch_offset_2600h fig/twitch_offset
#python wf-attack-vpn/plotter/plot_all.py twitch_offset_2_5h  wf-result/twitch_offset/twitch_offset_2_5h  fig/twitch_offset

# rnd, sample 20
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_20_100h wf-result/twitch_rnd_20/twitch_rnd_100h  fig/twitch_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_20_2h   wf-result/twitch_rnd_20/twitch_rnd_2h    fig/twitch_rnd
# rnd, sample 100
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_100h wf-result/twitch_rnd_100/twitch_rnd_100h  fig/twitch_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_2h   wf-result/twitch_rnd_100/twitch_rnd_2h    fig/twitch_rnd

# div ittr, sample 20
#python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_20_2600h wf-result/twitch_div_ittr_20/twitch_div_ittr_2600h fig/twitch_div_ittr
#python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_20_2_5h  wf-result/twitch_div_ittr_20/twitch_div_ittr_2_5h  fig/twitch_div_ittr
# div ittr, sample 100
#python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_100_2600h wf-result/twitch_div_ittr_100/twitch_div_ittr_2600h fig/twitch_div_ittr
#python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_100_2_5h  wf-result/twitch_div_ittr_100/twitch_div_ittr_2_5h  fig/twitch_div_ittr

# Divided, randomized, sample 20
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_20_100h wf-result/twitch_div_rnd_20/twitch_div_rnd_100h fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_20_2h   wf-result/twitch_div_rnd_20/twitch_div_rnd_2h   fig/twitch_div_rnd
# Divided, randomized, sample 100
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_100h wf-result/twitch_div_rnd_100/twitch_div_rnd_100h fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_2h   wf-result/twitch_div_rnd_100/twitch_div_rnd_2h   fig/twitch_div_rnd

# cp files for the comparison

# 20 default
cp wf-result/undef_20/combined/combined.csv                      wf-result/compare_20_default/undef.csv
cp wf-result/twitch_old/old_twitch_20/default.csv                wf-result/compare_20_default/twitch.csv
cp wf-result/twitch_rnd_20/twitch_rnd_2h/default.csv             wf-result/compare_20_default/rnd.csv
cp wf-result/twitch_div_rnd_20/twitch_div_rnd_2h/default.csv     wf-result/compare_20_default/div-rnd.csv

# 20 constant
cp wf-result/undef_20/combined/combined.csv                       wf-result/compare_20_constant/undef.csv
cp wf-result/twitch_old/old_twitch_20/constant.csv                wf-result/compare_20_constant/twitch.csv
cp wf-result/twitch_rnd_20/twitch_rnd_2h/constant.csv             wf-result/compare_20_constant/rnd.csv
cp wf-result/twitch_div_rnd_20/twitch_div_rnd_2h/constant.csv     wf-result/compare_20_constant/div-rnd.csv

# 20 Tik-Tok
cp wf-result/undef_20/combined/combined.csv                     wf-result/compare_20_tiktok/undef.csv
cp wf-result/twitch_old/old_twitch_20/tiktok.csv                wf-result/compare_20_tiktok/twitch.csv
cp wf-result/twitch_rnd_20/twitch_rnd_2h/tiktok.csv             wf-result/compare_20_tiktok/rnd.csv
cp wf-result/twitch_div_rnd_20/twitch_div_rnd_2h/tiktok.csv     wf-result/compare_20_tiktok/div-rnd.csv

# 100 default
cp wf-result/undef_100/combined/combined.csv                      wf-result/compare_100_default/undef.csv
cp wf-result/twitch_old/old_twitch_100/default.csv                wf-result/compare_100_default/twitch.csv
cp wf-result/twitch_rnd_20/twitch_rnd_2h/default.csv              wf-result/compare_100_default/rnd.csv
cp wf-result/twitch_div_rnd_100/twitch_div_rnd_2h/default.csv     wf-result/compare_100_default/div-rnd.csv

# 100 constant
cp wf-result/undef_100/combined/combined.csv                       wf-result/compare_100_constant/undef.csv
cp wf-result/twitch_old/old_twitch_100/constant.csv                wf-result/compare_100_constant/twitch.csv
cp wf-result/twitch_rnd_20/twitch_rnd_2h/constant.csv              wf-result/compare_100_constant/rnd.csv
cp wf-result/twitch_div_rnd_100/twitch_div_rnd_2h/constant.csv     wf-result/compare_100_constant/div-rnd.csv

# 100 Tik-Tok
cp wf-result/undef_100/combined/combined.csv                     wf-result/compare_100_tiktok/undef.csv
cp wf-result/twitch_old/old_twitch_100/tiktok.csv                wf-result/compare_100_tiktok/twitch.csv
cp wf-result/twitch_rnd_20/twitch_rnd_2h/tiktok.csv              wf-result/compare_100_tiktok/rnd.csv
cp wf-result/twitch_div_rnd_100/twitch_div_rnd_2h/tiktok.csv     wf-result/compare_100_tiktok/div-rnd.csv


# The final comparison graph
python wf-attack-vpn/plotter/plot_all.py compare_20_constant  wf-result/compare_20_constant  fig/compare_20
python wf-attack-vpn/plotter/plot_all.py compare_20_default   wf-result/compare_20_default   fig/compare_20
python wf-attack-vpn/plotter/plot_all.py compare_20_tiktok    wf-result/compare_20_tiktok    fig/compare_20

python wf-attack-vpn/plotter/plot_all.py compare_100_constant  wf-result/compare_100_constant  fig/compare_100
python wf-attack-vpn/plotter/plot_all.py compare_100_default   wf-result/compare_100_default   fig/compare_100
python wf-attack-vpn/plotter/plot_all.py compare_100_tiktok    wf-result/compare_100_tiktok    fig/compare_100