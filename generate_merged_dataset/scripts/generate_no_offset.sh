#!/bin/bash

# generate all merged datasets when not using any offset, or any other method to reduce the risk of the WF to learn by unwanted patterns

# to run:
# ./wf-attack-vpn/generate_merged_dataset/scripts/generate_no_offset.sh

#python wf-attack-vpn/generate_merged_dataset/main.py
#foreground_traffic
#background_traffic/twitch.h5
#merged_traffic/twitch_no_offset/twitch_no_offset_2600h
#1

#python wf-attack-vpn/generate_merged_dataset/main.py
#foreground_traffic
#background_traffic/twitch.h5
#merged_traffic/twitch_no_offset/twitch_no_offset_5h
#500

python wf-attack-vpn/generate_merged_dataset/main.py
send "foreground_traffic\r"
send "background_traffic/twitch.h5\r"
send "merged_traffic/twitch_no_offset/twitch_no_offset_2.5h"
send "1000"

