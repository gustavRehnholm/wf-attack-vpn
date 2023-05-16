#!/usr/bin/env python3

import argparse
import os

'''
To run:
python wf-attack-vpn/merge_traffic/scripts/worst_case_mit.py --app vimeo -f merged_traffic/worst_case_a -m merged_traffic/worst_case_b

# merge the applications, so that one can be generated for the worst case
python wf-attack-vpn/merge_traffic/main.py -f netflix -b background_traffic/mit/vimeo.h5 -m merged_traffic/worst_case --bfold  
'''

ap = argparse.ArgumentParser()
ap.add_argument("--app"   , required = True , type = str, default = "")
ap.add_argument("-f"   , required = True , type = str, default = "")
ap.add_argument("-m"   , required = True , type = str, default = "")
args = vars(ap.parse_args())

def main():
    '''
    10-fold merge for an MIT application
    '''

    app = args["app"]
    f_path = args['f']
    m_path = args['m']

    for i in range(0,10):
        os.system(f"mkdir merged_traffic/worst_case/fold_{i}")
        os.system(f"python wf-attack-vpn/merge_traffic/main.py -f {f_path}/fold_{i} -b background_traffic/mit/{app}.h5 -m {m_path}/fold_{i} --bfold {i} --len 10000")
    
if __name__ == "__main__":
    main()