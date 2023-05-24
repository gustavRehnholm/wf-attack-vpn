#!/bin/bash
# To create all the combinations on how to to test the attacker with access to other background dataset

# to run:
# ./wf-attack-vpn/train_test_combinations/undef/combine_all_undef.sh

# structure deestination merged_traffic/combined/<train set>/<test set>/<fold>

#python wf-attack-vpn/train_test_combinations/undef/combine_undef_app.py --app vimeo
python wf-attack-vpn/train_test_combinations/undef/combine_undef_app.py --app netflix


python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/combined_undef_print -w 10 -g fig/combined_undef