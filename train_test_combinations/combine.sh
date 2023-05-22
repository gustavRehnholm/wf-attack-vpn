#!/bin/bash
# To create all the combinations on how to to test the attacker with access to other background dataset

# structure deestination merged_traffic/combined/<train set>/<test set>/<fold>

python wf-attack-vpn/train_test_combinations/combine_10fold_undef -app vimeo

#python wf-attack-vpn/train_test_combinations/combine.py --train foreground_traffic --test merged_traffic/mit_5k/vimeo/fold_5 --dest merged_traffic/combined/foreground/vimeo/fold_5