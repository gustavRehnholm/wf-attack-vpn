#!/bin/bash

# ./wf-attack-vpn/wf-attack/wf-attack.sh

# ittr-no offset
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_no_offset/twitch_ittr_no_offset_2600h wf-result/twitch/twitch_ittr_no_offset/twitch_no_offset_2600h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_no_offset/twitch_ittr_no_offset_5h    wf-result/twitch/twitch_ittr_no_offset/twitch_no_offset_5h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_no_offset/twitch_ittr_no_offset_2_5h  wf-result/twitch/twitch_ittr_no_offset/twitch_no_offset_2.5h

# ittr-offset
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_offset/twitch_offset_2600h wf-result/twitch/twitch_ittr_no_offset/twitch_no_offset_2600h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_offset/twitch_offset_5h    wf-result/twitch/twitch_ittr_no_offset/twitch_no_offset_5h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_ittr_offset/twitch_offset_2_5h  wf-result/twitch/twitch_ittr_no_offset/twitch_no_offset_2.5h

# rnd-no offset
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_5h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h

# rnd-offset
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2600h wf-result/twitch_rnd_offset/twitch_rnd_offset_2600h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_5h    wf-result/twitch_rnd_offset/twitch_rnd_offset_5h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2_5h  wf-result/twitch_rnd_offset/twitch_rnd_offset_2_5h

# divide
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2600h wf-result/twitch_div_ittr/twitch_div_ittr_2600h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_5h    wf-result/twitch_div_ittr/twitch_div_ittr_5h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_ittr/twitch_div_ittr_2_5h  wf-result/twitch_div_ittr/twitch_div_ittr_2_5h

# divide-rnd
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd/twitch_div_rnd_2600h wf-result/twitch_div_rnd/twitch_div_rnd_2600h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd/twitch_div_rnd_5h    wf-result/twitch_div_rnd/twitch_div_rnd_5h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_div_rnd/twitch_div_rnd_2_5h  wf-result/twitch_div_rnd/twitch_div_rnd_2_5h
