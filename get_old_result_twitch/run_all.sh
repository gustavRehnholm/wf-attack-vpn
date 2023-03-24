#!/bin/bash
# ./wf-attack-vpn/get_old_result_twitch/run_all.sh

# rm broken files
python wf-attack-vpn/get_old_result_twitch/rm_broken_files.py

# parse as rds-collect did
python wf-attack-vpn/get_old_result_twitch/parse.py

# replicate their wf attack (and they used sample 20)
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/old_twitch wf-result/old_twitch 20

# plot the result (as they did)
python wf-attack-vpn/plotter/plot_all.py twitch_old wf-result/old_twitch fig/twitch_old