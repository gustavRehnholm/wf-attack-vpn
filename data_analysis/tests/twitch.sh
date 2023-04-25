#!/bin/bash
# Test to get the start of the foreground traffic, by testing against the capture file with the highest density of packets

# to run:
# ./wf-attack-vpn/data_analysis/tests/twitch.sh

# merge 
#python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_40.h5 -m merged_traffic/test/40/twitch_10_10 --ffold 0 -w 1
#python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_40.h5 -m merged_traffic/test/40/twitch_0     --ffold 0 -w 1

# analysis
#python wf-attack-vpn/data_analysis/merged-foreground-ratio.py -d merged_traffic/test/40/twitch_10_10
#python wf-attack-vpn/data_analysis/merged-foreground-ratio.py -d merged_traffic/test/40/twitch_0

# wf attack 
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/40/twitch_0     -r wf-result/twitch_40/twitch_0  -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/test/40/twitch_10_10 -r wf-result/twitch_40/twitch_10 -s 100

# plot
python wf-attack-vpn/plotter/plot_all.py --title twitch_0     --input wf-result/twitch_40/twitch_0     --output fig/twitch_40
python wf-attack-vpn/plotter/plot_all.py --title twitch_10_10 --input wf-result/twitch_40/twitch_10    --output fig/twitch_40