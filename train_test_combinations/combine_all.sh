#!/bin/bash
# To create all the combinations on how to to test the attacker with access to other background dataset

# structure deestination merged_traffic/combined/<train set>/<test set>/<fold>

python wf-attack-vpn/train_test_combinations/combine_undef_app.py --app vimeo