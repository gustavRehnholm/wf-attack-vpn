# create the worst case for the MIT dataset

# youtube and vimeo
#python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app vimeo      --len 10000
#python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app youtube    --len 10000
#python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app vimeo -f merged_traffic/mit/youtube -m merged_traffic/worst_case_a
#rm -f -r merged_traffic/mit/youtube
#rm -f -r merged_traffic/mit/vimeo

# netflix, youtube and vimeo
#python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app netflix    --len 10000
#python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app netflix -f merged_traffic/worst_case_a -m merged_traffic/worst_case_b
#rm -f -r merged_traffic/mit/netflix

# added RDP
#python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app rdp        --len 10000
#python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app rdp -f merged_traffic/worst_case_b -m merged_traffic/worst_case_a
#rm -f -r merged_traffic/mit/rdp

# added skype
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app skype-chat        --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app skype-chat -f merged_traffic/worst_case_a -m merged_traffic/worst_case_b
rm -f -r merged_traffic/mit/skype-chat

# added ssh
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app ssh        --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app ssh -f merged_traffic/worst_case_b -m merged_traffic/worst_case_a
rm -f -r merged_traffic/mit/ssh

# added voip
python wf-attack-vpn/merge_traffic/scripts/run_mit.py --app voip        --len 10000
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app voip -f merged_traffic/worst_case_a -m merged_traffic/worst_case_b
rm -f -r merged_traffic/mit/voip