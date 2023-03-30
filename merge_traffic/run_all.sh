#!/bin/bash
# {foreground} {background} {merged} {fold}

# ./wf-attack-vpn/merge_traffic/run_all.sh

python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_200.h5 merged_traffic/twitch_div_rnd_200 1
python wf-attack-vpn/merge_traffic/main.py foreground_traffic background_traffic/twitch_1.h5   merged_traffic/twitch_div_rnd_1   1
