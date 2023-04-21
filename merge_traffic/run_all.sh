#!/bin/bash
# To create all the merged sets from the twitch dataset.
# the input is ordered as:
# {foreground} {background} {merged} {fold}

# to run:
# ./wf-attack-vpn/merge_traffic/run_all.sh

# merge 

python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf-result/twitch_div_rnd/twitch_div_rnd_middle_2h  -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_last   -r wf-result/twitch_div_rnd/twitch_div_rnd_last_2h    -s 100

# divided
#python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_50.h5       -m merged_traffic/twitch_div_rnd_50       --fold 0 -w 1
#python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_first.h5  -m merged_traffic/twitch_div_rnd_1_first  --fold 0 -w 5
#python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_last.h5   -m merged_traffic/twitch_div_rnd_1_last   --fold 0 -w 5
#python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_middle.h5 -m merged_traffic/twitch_div_rnd_1_middle --fold 0 -w 5

# non-divided
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_50.h5       -m merged_traffic/twitch_rnd_50       --fold 0 -w 1
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_first.h5  -m merged_traffic/twitch_rnd_1_first  --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_last.h5   -m merged_traffic/twitch_rnd_1_last   --fold 0 -w 5
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_middle.h5 -m merged_traffic/twitch_rnd_1_middle --fold 0 -w 5

# WF attack

# non-divided
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_50        -r wf-result/twitch_rnd_100/twitch_rnd_100h               -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_first   -r wf-result/twitch_div_rnd_100/twitch_div_rnd_first_2h   -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_last    -r wf-result/twitch_div_rnd_100/twitch_div_rnd_last_2h    -s 100
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle  -r wf-result/twitch_div_rnd_100/twitch_div_rnd_middle_2h  -s 100

# divided
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_50       -r wf-result/twitch_div_rnd/twitch_div_rnd_100h       -s 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_first  -r wf-result/twitch_div_rnd/twitch_div_rnd_first_2h   -s 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_last   -r wf-result/twitch_div_rnd/twitch_div_rnd_last_2h    -s 100
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf-result/twitch_div_rnd/twitch_div_rnd_middle_2h  -s 100

./wf-attack-vpn/plotter/plot.sh