#!/bin/bash

'''
Run DF (with all three modes) on the merged datasets with MIT
./wf-attack-vpn/wf-attack/run_all_mit.sh
'''

# should take roughly 5 h per 10-fold (total of 35h)
# double the time of 10,000 lines per file is used (--len10k True)

python wf-attack-vpn/wf-attack/wf_mit.py --app voip
python wf-attack-vpn/wf-attack/wf_mit.py --app rdp
python wf-attack-vpn/wf-attack/wf_mit.py --app vimeo
python wf-attack-vpn/wf-attack/wf_mit.py --app netflix 
python wf-attack-vpn/wf-attack/wf_mit.py --app skype-chat
python wf-attack-vpn/wf-attack/wf_mit.py --app ssh
python wf-attack-vpn/wf-attack/wf_mit.py --app youtube

python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/mit/ -g fig/mit/ -w 10 --ylim_lower 0