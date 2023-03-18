#!/bin/bash

# generate all merged datasets when using rnd chunk, but no offset, or any other method to reduce the risk of the WF to learn by unwanted patterns

# to run:
# ./wf-attack-vpn/generate_merged_dataset/scripts/rnd.sh

python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h 1

python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h 500

python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h 1000

