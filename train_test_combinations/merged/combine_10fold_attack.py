#!/usr/bin/env python3

import os

def combine_10fold_attack(title):

    print("Start wf attack on combined 10-fold")

    os.system(f"mkdir wf_result/combine_merged/{title}")
    for i in range(0,10):
        os.system(f"mkdir mkdir wf_result/combine_merged/{title}/fold_{i}")

        os.system(f"python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/combined/merged/{title}/fold_{i}/client -r wf_result/combine_merged/{title}/fold_{i} -s 100 --epochs 30")
    
