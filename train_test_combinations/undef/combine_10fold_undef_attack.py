#!/usr/bin/env python3

import os

def combine_10fold_undef_attack(app):

    print("Start wf attack on combined 10-fold")

    os.system(f"mkdir wf_result/combined_undef/{app}")
    for i in range(0,10):
        os.system(f"mkdir wf_result/combined_undef/{app}/fold_{i}")
        os.system(f"python wf-attack-vpn/wf-attack/wf-attack-dir.py -m merged_traffic/combined/foreground/{app}/fold_{i}/client -r wf_result/combined_undef/{app}/fold_{i} -s 100 --epochs 30")
    
if __name__ == "__main__":
    main()