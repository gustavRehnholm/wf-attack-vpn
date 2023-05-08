#!/bin/bash
# To create all the merged sets from the twitch dataset.

# to run:
# ./wf-attack-vpn/merge_traffic/run_all_mit.sh

# merge 

# voip
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_0 --bfold 0 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_1 --bfold 1 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_2 --bfold 2 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_3 --bfold 3 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_4 --bfold 4 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_5 --bfold 5 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_6 --bfold 6 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_7 --bfold 7 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_8 --bfold 8 -w 10
python wf-attack-vpn/merge_traffic/main.py -b mit/parsed_app/voip.h5 -m merged_traffic/voip_9 --bfold 9 -w 10