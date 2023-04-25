#!/bin/bash
# Test to get the start of the foreground traffic, by testing against the capture file with the highest density of packets

# to run:
# ./wf-attack-vpn/data_analysis/tests/twitch_0.sh

# merge 
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/0/twitch --fold 0 -w 5
# analysis
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/0/twitch


