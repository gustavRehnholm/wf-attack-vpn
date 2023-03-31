#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# undefended plot
python wf-attack-vpn/plotter/plot_all.py twitch_undef wf-result/undef/10-fold fig/undef
# replicated twitch dataset
python wf-attack-vpn/plotter/plot_all.py twitch_old_og  wf-result/twitch_old/old_twitch_og  fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py twitch_old_20  wf-result/twitch_old/old_twitch_20  fig/twitch_old
python wf-attack-vpn/plotter/plot_all.py twitch_old_100 wf-result/twitch_old/old_twitch_100 fig/twitch_old
# The final comparison graph
python wf-attack-vpn/plotter/plot_all.py compare wf-result/compare fig/compare
# offset. sample 20
python wf-attack-vpn/plotter/plot_all.py twitch_offset_2600h wf-result/twitch_offset/twitch_offset_2600h fig/twitch_offset
python wf-attack-vpn/plotter/plot_all.py twitch_offset_2_5h  wf-result/twitch_offset/twitch_offset_2_5h  fig/twitch_offset
# rnd, sample 20
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_20_150h wf-result/twitch_rnd_20/twitch_rnd_300h  fig/twitch_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_20_2h   wf-result/twitch_rnd_20/twitch_rnd_2h    fig/twitch_rnd
# rnd, sample 100
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_150h wf-result/twitch_rnd_100/twitch_rnd_300h  fig/twitch_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_100_2h   wf-result/twitch_rnd_100/twitch_rnd_2h    fig/twitch_rnd
# div ittr, sample 20
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_20_2600h wf-result/twitch_div_ittr_20/twitch_div_ittr_2600h fig/twitch_div_ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_20_2_5h  wf-result/twitch_div_ittr_20/twitch_div_ittr_2_5h  fig/twitch_div_ittr
# div ittr, sample 20
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_100_2600h wf-result/twitch_div_ittr_100/twitch_div_ittr_2600h fig/twitch_div_ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_100_2_5h  wf-result/twitch_div_ittr_100/twitch_div_ittr_2_5h  fig/twitch_div_ittr
# Divided, randomized, sample 20
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_20_300h wf-result/twitch_div_rnd_20/twitch_div_rnd_300h fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_20_2h   wf-result/twitch_div_rnd_20/twitch_div_rnd_2h   fig/twitch_div_rnd
# Divided, randomized, sample 100
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_300h wf-result/twitch_div_rnd_100/twitch_div_rnd_300h fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_2h   wf-result/twitch_div_rnd_100/twitch_div_rnd_2h   fig/twitch_div_rnd