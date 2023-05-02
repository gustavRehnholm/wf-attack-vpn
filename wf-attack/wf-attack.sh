#!/bin/bash

'''
Run DF (with all three modes) on the merged datasets
./wf-attack-vpn/wf-attack/wf-attack.sh
'''

# non-divided
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_40       -r wf_result/twitch_rnd/twitch_rnd_80h       -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_first  -r wf_result/twitch_rnd/twitch_rnd_first_2h  -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_last   -r wf_result/twitch_rnd/twitch_rnd_last_2h   -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd/twitch_rnd_middle_2h -s 100 --epochs 30

# divide, randomized order
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_40       -r wf_result/twitch_div_rnd/twitch_div_rnd_80h        -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_first  -r wf_result/twitch_div_rnd/twitch_div_rnd_first_2h   -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_last   -r wf_result/twitch_div_rnd/twitch_div_rnd_last_2h    -s 100 --epochs 30
python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd/twitch_div_rnd_middle_2h  -s 100 --epochs 30

# higher epochs, divide
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd_epoch/twitch_div_rnd_middle_2h_epoch_60   -s 100 --epochs 60
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd_epoch/twitch_div_rnd_middle_2h_epoch_300  -s 100 --epochs 300
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_div_rnd_1_middle -r wf_result/twitch_div_rnd_epoch/twitch_div_rnd_middle_2h_epoch_1000 -s 100 --epochs 1000

# non-divided, with higher epoch
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd_epoch/twitch_rnd_middle_2h_epoch_60   -s 100 --epochs 60
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd_epoch/twitch_rnd_middle_2h_epoch_300  -s 100 --epochs 300
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/twitch_rnd_1_middle -r wf_result/twitch_rnd_epoch/twitch_rnd_middle_2h_epoch_1000 -s 100 --epochs 1000

./wf-attack-vpn/plot_graphs/plot.sh