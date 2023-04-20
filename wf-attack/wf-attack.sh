#!/bin/bash

# ./wf-attack-vpn/wf-attack/wf-attack.sh

# non divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_50 -r wf-result/twitch_rnd_100/twitch_rn_100h
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1   -r wf-result/twitch_rnd_100/twitch_rnd_2h

# divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_50 -r wf-result/twitch_div_rnd_100/twitch_div_rnd_100h
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1   -r wf-result/twitch_div_rnd_100/twitch_div_rnd_2h
