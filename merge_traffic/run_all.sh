#!/bin/bash
# To create all the merged sets from the twitch dataset.
# the input is ordered as:
# {foreground} {background} {merged} {fold}

# to run:
# ./wf-attack-vpn/merge_traffic/run_all.sh

#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_50.h5       merged_traffic/twitch_div_rnd_50      0
#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1_first.h5  merged_traffic/twitch_div_rnd_1_first 0
#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1_last.h5   merged_traffic/twitch_div_rnd_1_last  0

#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_50.h5       merged_traffic/twitch_rnd_50      0
#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1_first.h5  merged_traffic/twitch_rnd_1_first 0
#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1_last.h5   merged_traffic/twitch_rnd_1_last  0

# wf attack
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_50      wf-result/twitch_rnd_100/twitch_rnd_100h             100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_1_first wf-result/twitch_div_rnd_100/twitch_div_rnd_first_2h 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_1_last  wf-result/twitch_div_rnd_100/twitch_div_rnd_last_2h  100

# divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_50      -r wf-result/twitch_div_rnd_100/twitch_div_rnd_100h     -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_first -r wf-result/twitch_div_rnd_100/twitch_div_rnd_first_2h -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_last  -r wf-result/twitch_div_rnd_100/twitch_div_rnd_last_2h  -s 100

./wf-attack-vpn/plotter/plot.sh