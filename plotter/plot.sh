#!/bin/bash

# ./wf-attack-vpn/plotter/plot.sh

# plot the compare graph
python wf-attack-vpn/plotter/plot_all.py compare wf-result/combined fig/combined

# offset
python wf-attack-vpn/plotter/plot_all.py twitch_ittr_offset_2600h wf-result/twitch_ittr_offset/twitch_ittr_offset_2600h fig/twitch_offset
python wf-attack-vpn/plotter/plot_all.py twitch_ittr_offset_2_5h  wf-result/twitch_ittr_offset/twitch_ittr_offset_2_5h  fig/twitch_offset

# rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_150h wf-result/twitch_rnd/twitch_rnd_150  fig/twitch_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_rnd_2h   wf-result/twitch_rnd/twitch_rnd_1    fig/twitch_rnd

# div ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_2600h wf-result/twitch_div_ittr/twitch_div_ittr_2600h fig/twitch_div_ittr
python wf-attack-vpn/plotter/plot_all.py twitch_div_ittr_2_5h  wf-result/twitch_div_ittr/twitch_div_ittr_2_5h  fig/twitch_div_ittr

# div rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_20_300h wf-result/twitch_div_rnd_20/twitch_div_rnd_300h fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_20_2h   wf-result/twitch_div_rnd_20/twitch_div_rnd_2h   fig/twitch_div_rnd

python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_300h wf-result/twitch_div_rnd_100/twitch_div_rnd_300h fig/twitch_div_rnd
python wf-attack-vpn/plotter/plot_all.py twitch_div_rnd_100_2h   wf-result/twitch_div_rnd_100/twitch_div_rnd_2h   fig/twitch_div_rnd