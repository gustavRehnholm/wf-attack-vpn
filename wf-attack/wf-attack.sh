#!/bin/bash

# ./wf-attack-vpn/wf-attack/wf-attack.sh

# non divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_rnd_100/twitch_rn_300h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_rnd_100/twitch_rnd_2h  100

# divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_div_rnd_100/twitch_div_rnd_300h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_div_rnd_100/twitch_div_rnd_2h   100
