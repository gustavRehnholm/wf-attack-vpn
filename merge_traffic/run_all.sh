#!/bin/bash
# To create all the merged sets from the twitch dataset.

# to run:
# ./wf-attack-vpn/merge_traffic/run_all.sh

# merge 

# divided
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_40.h5       -m merged_traffic/twitch_div_rnd_40       --ffold 0 --bfold 1 -w 1 --div True
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_first.h5  -m merged_traffic/twitch_div_rnd_1_first  --ffold 0 --bfold 1 -w 5 --div True
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_last.h5   -m merged_traffic/twitch_div_rnd_1_last   --ffold 0 --bfold 1 -w 5 --div True
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_middle.h5 -m merged_traffic/twitch_div_rnd_1_middle --ffold 0 --bfold 1 -w 5 --div True

# non-divided
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_40.h5       -m merged_traffic/twitch_rnd_40       --ffold 0 --bfold 1 -w 1 --div False
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_first.h5  -m merged_traffic/twitch_rnd_1_first  --ffold 0 --bfold 1 -w 5 --div False
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_last.h5   -m merged_traffic/twitch_rnd_1_last   --ffold 0 --bfold 1 -w 5 --div False
python wf-attack-vpn/merge_traffic/main.py -f foreground_traffic -b background_traffic/twitch_1_middle.h5 -m merged_traffic/twitch_rnd_1_middle --ffold 0 --bfold 1 -w 5 --div False