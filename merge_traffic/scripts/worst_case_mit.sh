# create the worst case for the MIT dataset
# it will need two worst case sets (a and b), one for the previouse result adn one for the new one. The result will be in the subset b

# the merged datasets use upp a lot of disk space, so it will delete the merged datasets for each application while it run
# it uses 10k packets, to prevent that the foregorund gets lost in all the backgorund packets

# Requirment:
# have parsed MIT background dataset for the 7 applications that was not a filetransfere (vimeo, youtube, netflix, rdp, skype, ssh, and voip)

# to run:
# ./wf-attack-vpn/merge_traffic/scripts/worst_case_mit.sh

# youtube and vimeo
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app vimeo      --len 10000
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app youtube    --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app vimeo -f merged_traffic/mit/youtube -m merged_traffic/worst_case_a
rm -f -r merged_traffic/mit/youtube
rm -f -r merged_traffic/mit/vimeo

# netflix, youtube and vimeo
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app netflix --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app netflix -f merged_traffic/worst_case_a -m merged_traffic/worst_case_b
rm -f -r merged_traffic/mit/netflix

# added RDP
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app rdp --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app rdp -f merged_traffic/worst_case_b -m merged_traffic/worst_case_a
rm -f -r merged_traffic/mit/rdp

# added skype
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app skype-chat --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app skype-chat -f merged_traffic/worst_case_a -m merged_traffic/worst_case_b
rm -f -r merged_traffic/mit/skype-chat

# added ssh
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app ssh --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app ssh -f merged_traffic/worst_case_b -m merged_traffic/worst_case_a
rm -f -r merged_traffic/mit/ssh

# added voip
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app voip --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app voip -f merged_traffic/worst_case_a -m merged_traffic/worst_case_b
rm -f -r merged_traffic/mit/voip
rm -f -r merged_traffic/worst_case_a

# get WF result (5k and 10k packets per file)
python wf-attack-vpn/wf-attack/wf_mit_worst_case.py --lenpkt 5000
python wf-attack-vpn/wf-attack/wf_mit_worst_case.py --lenpkt 10000

# printable result for the worst case (restructure, so that it becomes one graph per mode, not per fold)
python wf-attack-vpn/wf-attack/worst_case_print.py -r worst_case_print_10k -i worst_case_10k
python wf-attack-vpn/wf-attack/worst_case_print.py -r worst_case_print_5k  -i worst_case_5k

# print the printable result
python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/worst_case_print_10k/ -g fig/mit/ -w 10 --ylim_lower 0
python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/worst_case_print_5k/ -g fig/mit/ -w 10 --ylim_lower 0

# analyse overhead on 5k and 10k
python wf-attack-vpn/data_analysis/analyze_all_merged.py -i merged_traffic/worst_case_b -r overhead/worst_case_10k --lenpkt 10000
python wf-attack-vpn/data_analysis/analyze_all_merged.py -i merged_traffic/worst_case_b -r overhead/worst_case_5k  --lenpkt 5000