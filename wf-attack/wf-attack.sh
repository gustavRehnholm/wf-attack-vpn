#!/bin/bash

# ./wf-attack-vpn/wf-attack/wf-attack.sh

# non divided, non randomized, but with an offset
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_offset/twitch_ittr_offset_2600h wf-result/twitch_ittr_offset/twitch_ittr_offset_2600h 20
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_offset/twitch_ittr_offset_2_5h  wf-result/twitch_ittr_offset/twitch_ittr_offset_2_5h  20

# non divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_rnd_20/twitch_rnd_300h 20
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_rnd_20/twitch_rnd_2h   20

python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_rnd_100/twitch_rn_300h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_rnd_100/twitch_rnd_2h   100

# divide, non randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2600h wf-result/twitch_div_ittr_20/twitch_div_ittr_2600h 20
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2_5h  wf-result/twitch_div_ittr_20/twitch_div_ittr_2_5h  20

python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2600h wf-result/twitch_div_ittr_100/twitch_div_ittr_2600h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2_5h  wf-result/twitch_div_ittr_100/twitch_div_ittr_2_5h  100

# divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_div_rnd_20/twitch_div_rnd_300h 20
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_div_rnd_20/twitch_div_rnd_2h   20

python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_150 wf-result/twitch_div_rnd_100/twitch_div_rnd_300h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd_1   wf-result/twitch_div_rnd_100/twitch_div_rnd_2h   100
