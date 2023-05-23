#!/bin/bash

'''
Run DF (with all three modes) on the merged datasets with Twitch
./wf-attack-vpn/wf-attack/wf-twitch.sh
'''

# rnd
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_40       -r wf_result/twitch_rnd/all_80h   -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_first  -r wf_result/twitch_rnd/first_2h  -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd/middle_2h -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_last   -r wf_result/twitch_rnd/last_2h   -s 100 --epochs 30

# div-rnd
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_40       -r wf_result/twitch_div_rnd/all_80h   -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_first  -r wf_result/twitch_div_rnd/first_2h  -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd/middle_2h -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_last   -r wf_result/twitch_div_rnd/last_2h   -s 100 --epochs 30


# higher epochs, div-rnd
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd_epoch/_2h_epoch_60   -s 100 --epochs 60
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd_epoch/_2h_epoch_300  -s 100 --epochs 300
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd_epoch/_2h_epoch_1000  -s 100 --epochs 1000

# higher epochs, rnd
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd_epoch/_2h_epoch_60   -s 100 --epochs 60
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd_epoch/_2h_epoch_300  -s 100 --epochs 300
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd_epoch/_2h_epoch_1000  -s 100 --epochs 1000

./wf-attack-vpn/plot_graphs/plot.sh