#!/bin/bash
# Test to get the start of the foreground traffic, by testing against the capture file with the highest density of packets

# to run:
# ./wf-attack-vpn/data_analysis/tests/twitch_10_01.sh

# merge 
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/10_01/twitch_largest_1 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/10_01/twitch_largest_2 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/10_01/twitch_largest_3 --fold 0 -w 5

# analysis
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/10_01/twitch_largest_1
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/10_01/twitch_largest_2
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/10_01/twitch_largest_3