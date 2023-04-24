#!/bin/bash
# Test to get the start of the foreground traffic, by testing against the capture file with the highest density of packets

# to run:
# ./wf-attack-vpn/merge_traffic/run_all_tmp.sh

# merge 
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/0/twitch_largest_1 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/0/twitch_largest_2 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/0/twitch_largest_3 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/0/twitch_largest_4 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/0/twitch_largest_5 --fold 0 -w 5

# WF attack
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/0/twitch_largest_1 -r wf-result/test/0/twitch_largest_1 -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/0/twitch_largest_2 -r wf-result/test/0/twitch_largest_2 -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/0/twitch_largest_3 -r wf-result/test/0/twitch_largest_3 -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/0/twitch_largest_4 -r wf-result/test/0/twitch_largest_4 -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/0/twitch_largest_5 -r wf-result/test/0/twitch_largest_5 -s 100

