#!/bin/bash
# Test to get the start of the foreground traffic, by testing against the capture file with the highest density of packets

# to run:
# ./wf-attack-vpn/data_analysis/tests/twitch_5_100.sh

# merge 
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_last.h5  -m merged_traffic/test/5_100/twitch --fold 0 -w 5

# analysis
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/5_100/twitch