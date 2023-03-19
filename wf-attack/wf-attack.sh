#!/bin/bash

# ./wf-attack-vpn/wf-attack/wf-attack.sh

# naive approach: no offset
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_no_offset/twitch_no_offset_2600h wf-result/twitch/twitch_no_offset/twitch_no_offset_2600h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_no_offset/twitch_no_offset_5h wf-result/twitch/twitch_no_offset/twitch_no_offset_5h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_no_offset/twitch_no_offset_2_5h wf-result/twitch/twitch_no_offset/twitch_no_offset_2.5h

# nonly offset
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_offset/twitch_offset_2600h wf-result/twitch/twitch_no_offset/twitch_no_offset_2600h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_offset/twitch_offset_5h    wf-result/twitch/twitch_no_offset/twitch_no_offset_5h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_offset/twitch_offset_2_5h  wf-result/twitch/twitch_no_offset/twitch_no_offset_2.5h

# with only randomize
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_5h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h

# rnd-offset
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_5h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h

# divide
# divide-rnd

