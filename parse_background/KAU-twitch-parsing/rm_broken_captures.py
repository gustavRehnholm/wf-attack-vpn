#!/usr/bin/python3

'''
rm the capture files that are broken (lack sufficient captures)

TODO: make the cleaning automatic
'''

import pandas as pd
import shutil
import os

# the known unusable files, check that they are removed
BROKEN_FILES_1 = [
    "tshark_1.9h_twitch-chess_stream_2022-12-26.h5",
    "tshark_1.9h_twitch-public_domain_television_stream_2022-12-17.h5",
    "tshark_1.9h_twitch-reallyreallylongathon_stream_2022-12-26.h5",
    "tshark_1.9h_twitch-retrolongplay_stream_2022-12-17_9.h5",
    "tshark_1.9h_twitch-retrolongplay_stream_2022-12-18_5.h5",
    "tshark_1.9h_twitch-ridingtherailstv_stream_2022-12-17_3.h5",
    "tshark_1.9h_twitch-smilesguthrie_stream_2022-12-24_1.h5",
    "tshark_1.9h_twitch-thorlar_stream_2022-12-25.h5",
    "tshark_1.9h_twitch-worldoftanks_stream_2022-12-23.h5",
    "tshark_1.9h_twitch-yungdingo_stream_2022-12-24.h5"
]

BROKEN_FILES_2 = [
    "tshark_1.9h_twitch-bridgetcase_stream_2022-12-29.h5",
    "tshark_1.9h_twitch-caedrel_stream_2023-01-04.h5",
    "tshark_1.9h_twitch-ccm6403_stream_2023-01-03.h5",
    "tshark_1.9h_twitch-lvndmark_stream_2022-12-31.h5",
    "tshark_1.9h_twitch-officialandypyro_stream_2023-01-07.h5",
    "tshark_1.9h_twitch-reallyreallylongathon_stream_2022-12-29_10.h5",
    "tshark_1.9h_twitch-thewillhallexp_stream_2022-12-31_6.h5",
    "tshark_1.9h_twitch-zalphx_stream_2023-01-05.h5"
]

BAD_FILES = [
    "tshark_2h_twitch-pdcinema_stream_2022-12-15.h5",
    "tshark_8h_twitch-fgfm_stream_2022-12-15.h5",
    "tshark_8h_twitch-pdcinema_stream_2022-12-15.h5",
    "tshark_10h_twitch-fgfm_stream_2022-12-14.h5",
    "tshark_10h_twitch-pdcinema_stream_2022-12-14.h5"
]

def main():
    print("Start the removal of unusable files")

    # the captures in h5 format
    DIR_INPUT = "twitch/raw_captures_h5/"
    # the usable captures
    DIR_OUTPUT = "twitch/usable_captures_h5/"

    COL_NAMES =  ['time', 'sender', 'receiver', 'size']

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)


    index = 0
    for file in os.listdir(DIR_INPUT):

        filename = os.fsdecode(file)
        index += 1
        print("")
        print("checking file " + str(index) + "/1370: " + str(filename))

        if filename in BROKEN_FILES_1:
            print("Removing file: " + filename)
            continue
        elif filename in BROKEN_FILES_2:
            print("Removing file: " + filename)
            continue
        elif filename in BAD_FILES:
            print("Removing file: " + filename)
            continue
        else:
            print("Keeping file: " + filename)
            src = DIR_INPUT + filename
            dst = DIR_OUTPUT + filename
            shutil.copyfile(src, dst)

# run main 
if __name__=="__main__":
    main()