#!/bin/bash

'''
Run DF (with all three modes) on the merged datasets with MIT
./wf-attack-vpn/wf-attack/wf-mit.sh
'''

# 10-fold voip
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_0 -r wf_result/mit/voip/fold_0 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_1 -r wf_result/mit/voip/fold_1 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_2 -r wf_result/mit/voip/fold_2 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_3 -r wf_result/mit/voip/fold_3 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_4 -r wf_result/mit/voip/fold_4 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_5 -r wf_result/mit/voip/fold_5 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_6 -r wf_result/mit/voip/fold_6 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_7 -r wf_result/mit/voip/fold_7 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_8 -r wf_result/mit/voip/fold_8 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/voip/voip_9 -r wf_result/mit/voip/fold_9 -s 100 --epochs 30

# 10-fold voip
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_0 -r wf_result/mit/rdp/fold_0 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_1 -r wf_result/mit/rdp/fold_1 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_2 -r wf_result/mit/rdp/fold_2 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_3 -r wf_result/mit/rdp/fold_3 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_4 -r wf_result/mit/rdp/fold_4 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_5 -r wf_result/mit/rdp/fold_5 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_6 -r wf_result/mit/rdp/fold_6 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_7 -r wf_result/mit/rdp/fold_7 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_8 -r wf_result/mit/rdp/fold_8 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/rdp/fold_9 -r wf_result/mit/rdp/fold_9 -s 100 --epochs 30

# 10-fold vimeo
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_0 -r wf_result/mit/vimeo/fold_0 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_1 -r wf_result/mit/vimeo/fold_1 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_2 -r wf_result/mit/vimeo/fold_2 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_3 -r wf_result/mit/vimeo/fold_3 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_4 -r wf_result/mit/vimeo/fold_4 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_5 -r wf_result/mit/vimeo/fold_5 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_6 -r wf_result/mit/vimeo/fold_6 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_7 -r wf_result/mit/vimeo/fold_7 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_8 -r wf_result/mit/vimeo/fold_8 -s 100 --epochs 30
#python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/mit/vimeo/fold_9 -r wf_result/mit/vimeo/fold_9 -s 100 --epochs 30

python wf-attack-vpn/wf-attack/wf_mit.py -app netflix

python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/mit/ -g fig/mit/ -w 10