#!/bin/bash
# To create all the merged sets from the twitch dataset.

# to run:
# ./wf-attack-vpn/merge_traffic/run_all_mit.sh

# create 10-fold merged datastes of the applications from the MIT dataset

python wf-attack-vpn/merge_traffic/run_mit.py -app netflix
python wf-attack-vpn/merge_traffic/run_mit.py -app rdp
python wf-attack-vpn/merge_traffic/run_mit.py -app skype-chat
python wf-attack-vpn/merge_traffic/run_mit.py -app ssh
python wf-attack-vpn/merge_traffic/run_mit.py -app vimeo
python wf-attack-vpn/merge_traffic/run_mit.py -app voip
python wf-attack-vpn/merge_traffic/run_mit.py -app youtube