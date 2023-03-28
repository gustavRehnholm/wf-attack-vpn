#!/bin/bash
# ./wf-attack-vpn/get_old_result_twitch/run_all.sh

# rm broken files
python wf-attack-vpn/get_old_result_twitch/rm_broken_files.py

# parse as rds-collect did, without bug
python wf-attack-vpn/get_old_result_twitch/parse.py

# parse as rds-collect did, with bug
python wf-attack-vpn/get_old_result_twitch/parse_og.py

# replicate their wf attack (and they used sample 20)
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/old_twitch_og wf-result/old_twitch_og 20
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/old_twitch wf-result/old_twitch_20    20
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/old_twitch wf-result/old_twitch_100  100

# plot the result (as they did)
python wf-attack-vpn/plotter/plot_all.py twitch_old_og  wf-result/old_twitch fig/twitch_old_og
python wf-attack-vpn/plotter/plot_all.py twitch_old_20  wf-result/old_twitch fig/twitch_old_20
python wf-attack-vpn/plotter/plot_all.py twitch_old_100 wf-result/old_twitch fig/twitch_old_100