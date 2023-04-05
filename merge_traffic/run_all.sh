#!/bin/bash
# To create all the merged sets from the twitch dataset.
# the input is ordered as:
# {foreground} {background} {merged} {fold}

# to run:
# ./wf-attack-vpn/merge_traffic/run_all.sh

#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_150.h5 merged_traffic/twitch_div_rnd_150 1
python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1.h5   merged_traffic/twitch_div_rnd_1   1

#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_150.h5 merged_traffic/twitch_rnd_150 1
#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1.h5   merged_traffic/twitch_rnd_1   1

# wf attack
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_rnd_20/twitch_rnd_300h 20
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_rnd_20/twitch_rnd_2h   20

#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_150     wf-result/twitch_rnd_100/twitch_rnd_300h 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_rnd_100/twitch_rnd_2h   100

# divide, randomized order
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_div_rnd_20/twitch_div_rnd_300h 20
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_div_rnd_20/twitch_div_rnd_2h   20

#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_div_rnd_100/twitch_div_rnd_300h 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_div_rnd_100/twitch_div_rnd_2h   100

./wf-attack-vpn/plotter/plot.sh