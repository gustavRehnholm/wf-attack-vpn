#!/bin/bash
# ./wf-attack-vpn/get_old_result_twitch/run_all.sh

python wf-attack-vpn/get_old_result_twitch/rm_broken_files.py

python wf-attack-vpn/get_old_result_twitch/parse.py

python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/old_twitch wf-result/old_twitch 20

python wf-attack-vpn/plotter/plot_all.py twitch_old wf-result/old_twitch fig/twitch_old