#!/bin/bash

'''
Run DF (with all three modes) on the merged datasets
To run:
./wf-attack-vpn/wf-attack/wf-attack.sh
'''

# wf attack
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_50 -r wf-result/twitch_rnd_100/twitch_rnd_100h -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1  -r wf-result/twitch_rnd_100/twitch_rnd_2h   -s 100

# divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_50 -r wf-result/twitch_div_rnd_100/twitch_div_rnd_100h -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1  -r wf-result/twitch_div_rnd_100/twitch_div_rnd_2h   -s 100

