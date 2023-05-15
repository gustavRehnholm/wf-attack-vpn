#!/bin/bash
# To create all the merged sets from the twitch dataset.

# to run:
# ./wf-attack-vpn/merge_traffic/run_all_mit.sh

# create 10-fold merged datastes of the applications from the MIT dataset

# get all applications with the len 10,000
# done
#python wf-attack-vpn/merge_traffic/run_mit.py --app netflix    --len 10000
#python wf-attack-vpn/merge_traffic/run_mit.py --app vimeo      --len 10000
#python wf-attack-vpn/merge_traffic/run_mit.py --app youtube    --len 10000

# not done yeet
#python wf-attack-vpn/merge_traffic/run_mit.py --app rdp        --len 10000
#python wf-attack-vpn/merge_traffic/run_mit.py --app skype-chat --len 10000
#python wf-attack-vpn/merge_traffic/run_mit.py --app ssh        --len 10000
#python wf-attack-vpn/merge_traffic/run_mit.py --app voip       --len 10000

# create the worst case

# youtube and vimeo
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app vimeo
# netflix, youtube and vimeo
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app netflix