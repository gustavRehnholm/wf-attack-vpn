#!/bin/bash

'''
get print for all 10k mit results
./wf-attack-vpn/plot_graphs/mit_10k_print.sh
'''

#python wf-attack-vpn/plot_graphs/result_10k_print.py --app youtube -r mit_10k_print -i mit_10k
#python wf-attack-vpn/plot_graphs/result_10k_print.py --app netflix -r mit_10k_print -i mit_10k
#python wf-attack-vpn/plot_graphs/result_10k_print.py --app vimeo   -r mit_10k_print -i mit_10k

#python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/mit_10k_print/ -g fig/mit_10k/ -w 10 --ylim_lower 0

python wf-attack-vpn/data_analysis/analyze_all_merged.py -i merged_traffic/mit/youtube -r overhead/youtube_10k
python wf-attack-vpn/data_analysis/analyze_all_merged.py -i merged_traffic/mit/vimeo   -r overhead/vimeo_10k  
python wf-attack-vpn/data_analysis/analyze_all_merged.py -i merged_traffic/mit/netflix -r overhead/netflix_10k

