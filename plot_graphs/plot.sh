#!/bin/bash

# ./wf-attack-vpn/plot_graphs/plot.sh


# cp files for the comparison

# 100 default
#cp wf_result/undef_100/combined/combined.csv                     wf_result/compare/compare_default/undef.csv
cp wf_result/twitch_old/old_twitch_100/default.csv               wf_result/compare/compare_default/twitch.csv
cp wf_result/twitch_div_rnd/twitch_div_rnd_middle_2h/default.csv wf_result/compare/compare_default/div_rnd.csv
cp wf_result/twitch_rnd/twitch_rnd_middle_2h/default.csv         wf_result/compare/compare_default/rnd.csv

# 100 constant
#cp wf_result/undef_100/combined/combined.csv                      wf_result/compare/compare_constant/undef.csv
cp wf_result/twitch_old/old_twitch_100/constant.csv               wf_result/compare/compare_constant/twitch.csv
cp wf_result/twitch_div_rnd/twitch_div_rnd_middle_2h/constant.csv wf_result/compare/compare_constant/div_rnd.csv
cp wf_result/twitch_rnd/twitch_rnd_middle_2h/constant.csv         wf_result/compare/compare_constant/rnd.csv

# 100 Tik-Tok
cp wf_result/undef_100/combined/combined.csv                    wf_result/compare/compare_tiktok/undef.csv
cp wf_result/twitch_old/old_twitch_100/tiktok.csv               wf_result/compare/compare_tiktok/twitch.csv
cp wf_result/twitch_div_rnd/twitch_div_rnd_middle_2h/tiktok.csv wf_result/compare/compare_tiktok/div_rnd.csv
cp wf_result/twitch_rnd/twitch_rnd_middle_2h/tiktok.csv         wf_result/compare/compare_tiktok/rnd.csv

# plot all results
python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/ -w 10