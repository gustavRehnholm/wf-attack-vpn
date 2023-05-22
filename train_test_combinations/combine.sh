#!/bin/bash
# To create all the combinations on how to to test the attacker with access to other background dataset

python wf-attack-vpn/train_test_combinations/combine.py --train foreground_traffic --test merged_traffic/mit_5k/vimeo/fold_5