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

    DIR_FOREGROUND = input("Where is the foreground located?")
    DIR_BACKGROUND = input("Where is the background located?")
    DIR_MERGED     = input("Where should the merged traffic be stored")

    
    amount = input("How large part of the background traffic should be used? (1/input packets will be used)")
    if type(amount) is int:
        BACKGROUND_AMOUNT = amount
    else:
        print("the provided value is not an integer, aborting the program ")
        return


    #DIR_FOREGROUND = "foreground_traffic"
    #DIR_MERGED     = "merged_traffic/twitch_no_offset"

    #DIR_ALL_BACKGROUNDS = "background_traffic"
    #FILE_BACKBROUND     = "twitch.h5"
    #DIR_BACKGROUND      = DIR_ALL_BACKGROUNDS + "/" + FILE_BACKBROUND

    #BACKGROUND_AMOUNT = 1

    generateMergedTraffic(dir_foreground = DIR_FOREGROUND, dir_merged = DIR_MERGED, dir_background = DIR_BACKGROUND, background_amount = BACKGROUND_AMOUNT)

if __name__=="__main__":
    main()