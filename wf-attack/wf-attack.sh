#!/bin/bash

'''
Run DF (with all three modes) on the merged datasets
'''

# divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_50       -r wf-result/twitch_div_rnd/twitch_div_rnd_100h       -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_first  -r wf-result/twitch_div_rnd/twitch_div_rnd_first_2h   -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_last   -r wf-result/twitch_div_rnd/twitch_div_rnd_last_2h    -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf-result/twitch_div_rnd/twitch_div_rnd_middle_2h  -s 100