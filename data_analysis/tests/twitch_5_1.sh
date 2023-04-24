#!/bin/bash
# Test to get the start of the foreground traffic, by testing against the capture file with the highest density of packets

# to run:
# ./wf-attack-vpn/data_analysis/tests/twitch_5_largest.sh

# merge 
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/5/twitch_largest_1 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/5/twitch_largest_2 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/5/twitch_largest_3 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/5/twitch_largest_4 --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/test/twitch_largest.h5  -m merged_traffic/test/5/twitch_largest_5 --fold 0 -w 5

# analysis
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/5/twitch_largest_1
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/5/twitch_largest_2
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/5/twitch_largest_3
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/5/twitch_largest_4
python wf-attack-vpn/data_analysis/foreground_cleaning.py -d merged_traffic/test/5/twitch_largest_5

# WF attack
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/5/twitch_largest_1 -r wf-result/test/5/twitch_largest_1 -s 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/5/twitch_largest_2 -r wf-result/test/5/twitch_largest_2 -s 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/5/twitch_largest_3 -r wf-result/test/5/twitch_largest_3 -s 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/5/twitch_largest_4 -r wf-result/test/5/twitch_largest_4 -s 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/5/twitch_largest_5 -r wf-result/test/5/twitch_largest_5 -s 100

# plot
#python wf-attack-vpn/plotter/plot_all.py --title twitch_largest_1 --input wf-result/test/5/twitch_largest_1 --output fig/twitch_5_largest
#python wf-attack-vpn/plotter/plot_all.py --title twitch_largest_2 --input wf-result/test/5/twitch_largest_2 --output fig/twitch_5_largest
#python wf-attack-vpn/plotter/plot_all.py --title twitch_largest_3 --input wf-result/test/5/twitch_largest_3 --output fig/twitch_5_largest
#python wf-attack-vpn/plotter/plot_all.py --title twitch_largest_4 --input wf-result/test/5/twitch_largest_4 --output fig/twitch_5_largest
#python wf-attack-vpn/plotter/plot_all.py --title twitch_largest_5 --input wf-result/test/5/twitch_largest_5 --output fig/twitch_5_largest

