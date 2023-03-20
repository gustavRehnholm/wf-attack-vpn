#!/bin/bash

# ./wf-attack-vpn/wf-attack/wf-attack-100.sh

# rnd-no offset
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h wf-result/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    wf-result/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  wf-result/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  100

# rnd-offset
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2600h wf-result/twitch_rnd_offset/twitch_rnd_offset_2600h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_5h    wf-result/twitch_rnd_offset/twitch_rnd_offset_5h    100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2_5h  wf-result/twitch_rnd_offset/twitch_rnd_offset_2_5h  100

# divide
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2600h wf-result/twitch_div_ittr/twitch_div_ittr_2600h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_5h    wf-result/twitch_div_ittr/twitch_div_ittr_5h    100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2_5h  wf-result/twitch_div_ittr/twitch_div_ittr_2_5h  100

# divide-rnd
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd/twitch_div_rnd_2600h wf-result/twitch_div_rnd/twitch_div_rnd_2600h 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd/twitch_div_rnd_5h    wf-result/twitch_div_rnd/twitch_div_rnd_5h    100
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd/twitch_div_rnd_2_5h  wf-result/twitch_div_rnd/twitch_div_rnd_2_5h  100
