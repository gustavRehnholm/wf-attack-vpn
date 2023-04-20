#!/usr/bin/python3

import pandas as pd
import shutil
import os
from multiprocessing import Pool

BROKEN_FILES = [
    "tshark_1.9h_twitch-chess_stream_2022-12-26.h5",
    "tshark_1.9h_twitch-public_domain_television_stream_2022-12-17.h5",
    "tshark_1.9h_twitch-reallyreallylongathon_stream_2022-12-26.h5",
    "tshark_1.9h_twitch-retrolongplay_stream_2022-12-17_9.h5",
    "tshark_1.9h_twitch-retrolongplay_stream_2022-12-18_5.h5",
    "tshark_1.9h_twitch-ridingtherailstv_stream_2022-12-17_3.h5",
    "tshark_1.9h_twitch-smilesguthrie_stream_2022-12-24_1.h5",
    "tshark_1.9h_twitch-thorlar_stream_2022-12-25.h5",
    "tshark_1.9h_twitch-worldoftanks_stream_2022-12-23.h5",
    "tshark_1.9h_twitch-yungdingo_stream_2022-12-24.h5",
    "tshark_1.9h_twitch-bridgetcase_stream_2022-12-29.h5",
    "tshark_1.9h_twitch-lvndmark_stream_2022-12-31.h5",
    "tshark_1.9h_twitch-officialandypyro_stream_2023-01-07.h5",
    "tshark_1.9h_twitch-reallyreallylongathon_stream_2022-12-29_10.h5",
    "tshark_1.9h_twitch-zalphx_stream_2023-01-05.h5"
]

BAD_FILES = [
    "tshark_2h_twitch-pdcinema_stream_2022-12-15.h5",
    "tshark_8h_twitch-fgfm_stream_2022-12-15.h5",
    "tshark_8h_twitch-pdcinema_stream_2022-12-15.h5",
    "tshark_10h_twitch-fgfm_stream_2022-12-14.h5",
    "tshark_10h_twitch-pdcinema_stream_2022-12-14.h5"
]

FILES_2_CLIENTS = [
    "tshark_1.9h_twitch-ccm6403_stream_2023-01-03.h5",
    "tshark_1.9h_twitch-caedrel_stream_2023-01-04.h5",
    "tshark_1.9h_twitch-thewillhallexp_stream_2022-12-31_6.h5"
]

def main():
    '''
    rm the capture files that are broken (lack sufficient captures)
    '''
    print("Start the removal of unusable files")

    # the captures in h5 format
    DIR_INPUT = "twitch/raw_captures_h5/"
    # the usable captures
    DIR_OUTPUT = "twitch/usable_captures_h5/"

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    input = []
    for currFile in os.listdir(DIR_INPUT):
        input.append((currFile, DIR_INPUT, DIR_OUTPUT))

    p = Pool(10)
    p.starmap(rm_if_broken, input)


def rm_if_broken(file, dir_input, dir_output):

    filename = os.fsdecode(file)

    if filename in BROKEN_FILES:
        print("Removing file: " + filename)
    elif filename in FILES_2_CLIENTS:
        print("Removing file: " + filename)
    elif filename in BAD_FILES:
        print("Removing file: " + filename)
    else:
        print("Keeping file: " + filename)
        src = dir_input + filename
        dst = dir_output + filename
        shutil.copyfile(src, dst)

    return

# run main 
if __name__=="__main__":
    main()