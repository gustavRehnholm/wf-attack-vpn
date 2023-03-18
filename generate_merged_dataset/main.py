#!/usr/bin/python3

'''
This program creates the merged traffic, used to test the WF attacks capabilities

TODO:
Input (sys.argv):
[1] : chunk size
[2] : offsett for the test files
[3] : offset for the valid files
[4] : offset for the train files
[5] : directory for the foreground traffic to use
[6] : directory for the merged traffic to use
[7] : directory for the background traffic file to use

python wf-attack-vpn/generate_merged_dataset/main.py
'''


from generate_merged_traffic import generateMergedTraffic

def main():

   generateMergedTraffic()

if __name__=="__main__":
    main()