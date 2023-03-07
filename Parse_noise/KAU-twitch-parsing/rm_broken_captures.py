#!/usr/bin/python3

'''
rm the capture files that are broken (lack sufficient captures)

touch stdout/rm_broken_captures.txt
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/rm_broken_captures.py | tee stdout/rm_broken_captures.txt
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
    DIR_RAW_H5_NOISE = "twitch/raw_captures_h5/"
    # the usable captures
    DIR_RAW_USABLE_NOISE = "twitch/usable_captures_h5/"

    COL_NAMES =  ['time', 'sender', 'receiver', 'size']


    index = 0
    for file in os.listdir(DIR_RAW_H5_NOISE):

        filename = os.fsdecode(file)
        index += 1
        print("")
        print("checking file " + str(index) + "/1370: " + str(filename))
        print("")

        if filename in BROKEN_FILES_1:
            continue
        elif filename in BROKEN_FILES_2:
            continue
        elif filename in BAD_FILES:
            continue
        else:
            src = DIR_RAW_H5_NOISE + filename
            dst = DIR_RAW_USABLE_NOISE + filename
            shutil.copyfile(src, dst)


        #path = DIR_RAW_H5_NOISE + filename
        #df = pd.read_hdf(path, key=key)

        # check the data for holes of unusable, or no data
        # and if the total amount of unusable packets, or time between packets is to high
        #for row in df:
        #    print("todo")


        # if packet is usable, store it in the new direcotry


    # check if any bad packets is left in DIR_RAW_USABLE_NOISE

# run main 
if __name__=="__main__":
    main()