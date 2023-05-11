#!/bin/bash
# To create all the merged sets from the twitch dataset.

# to run:
# ./wf-attack-vpn/merge_traffic/run_all_mit.sh

# create 10-fold merged datastes of the applications from the MIT dataset

#python wf-attack-vpn/merge_traffic/run_mit.py --app netflix    --len 10000
python wf-attack-vpn/merge_traffic/run_mit.py --app rdp        --len 10000
python wf-attack-vpn/merge_traffic/run_mit.py --app skype-chat --len 10000
python wf-attack-vpn/merge_traffic/run_mit.py --app ssh        --len 10000
python wf-attack-vpn/merge_traffic/run_mit.py --app vimeo      --len 10000
python wf-attack-vpn/merge_traffic/run_mit.py --app voip       --len 10000
python wf-attack-vpn/merge_traffic/run_mit.py --app youtube    --len 10000