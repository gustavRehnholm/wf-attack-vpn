#!/bin/bash
# To create all the merged sets from the twitch dataset.
# the input is ordered as:
# {foreground} {background} {merged} {fold}

# to run:
# ./wf-attack-vpn/merge_traffic/run_all.sh

python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_150.h5 merged_traffic/twitch_div_rnd_150 1
python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1.h5   merged_traffic/twitch_div_rnd_1   1

#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_150.h5 merged_traffic/twitch_rnd_150 1
#python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1.h5   merged_traffic/twitch_rnd_1   1
