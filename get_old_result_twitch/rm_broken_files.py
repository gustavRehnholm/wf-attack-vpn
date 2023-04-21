#!/usr/bin/python3

import pandas as pd
import shutil
import os
from multiprocessing import Pool

# the known unusable files, check that they are removed
BROKEN_FILES_1 = [
    "tshark_1.9h_twitch-chess_stream_2022-12-26.log",
    "tshark_1.9h_twitch-public_domain_television_stream_2022-12-17.log",
    "tshark_1.9h_twitch-reallyreallylongathon_stream_2022-12-26.log",
    "tshark_1.9h_twitch-retrolongplay_stream_2022-12-17_9.log",
    "tshark_1.9h_twitch-retrolongplay_stream_2022-12-18_5.log",
    "tshark_1.9h_twitch-ridingtherailstv_stream_2022-12-17_3.log",
    "tshark_1.9h_twitch-smilesguthrie_stream_2022-12-24_1.log",
    "tshark_1.9h_twitch-thorlar_stream_2022-12-25.log",
    "tshark_1.9h_twitch-worldoftanks_stream_2022-12-23.log",
    "tshark_1.9h_twitch-yungdingo_stream_2022-12-24.log"
]

BROKEN_FILES_2 = [
    "tshark_1.9h_twitch-bridgetcase_stream_2022-12-29.log",
    "tshark_1.9h_twitch-caedrel_stream_2023-01-04.log",
    "tshark_1.9h_twitch-ccm6403_stream_2023-01-03.log",
    "tshark_1.9h_twitch-lvndmark_stream_2022-12-31.log",
    "tshark_1.9h_twitch-officialandypyro_stream_2023-01-07.log",
    "tshark_1.9h_twitch-reallyreallylongathon_stream_2022-12-29_10.log",
    "tshark_1.9h_twitch-thewillhallexp_stream_2022-12-31_6.log",
    "tshark_1.9h_twitch-zalphx_stream_2023-01-05.log"
]

BAD_FILES = [
    "tshark_2h_twitch-pdcinema_stream_2022-12-15.log",
    "tshark_8h_twitch-fgfm_stream_2022-12-15.log",
    "tshark_8h_twitch-pdcinema_stream_2022-12-15.log",
    "tshark_10h_twitch-fgfm_stream_2022-12-14.log",
    "tshark_10h_twitch-pdcinema_stream_2022-12-14.log"
]

def main():
    '''
    rm the capture files that are broken (lack sufficient captures)
    '''

    print("Start the removal of unusable files")

    # the captures in h5 format
    DIR_INPUT = "captures"
    # the usable captures
    DIR_OUTPUT = "captures_clean_test"

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)

    files = os.listdir(DIR_INPUT)

    input = []
    for i in files:
        input.append((i, ""))
    
    p = Pool(5)
    p.starmap(check_rm_file, input)

    return


def check_rm_file(file, tmp):
    filename = os.fsdecode(file)
    if filename in BROKEN_FILES_1:
        print("Removing file: " + filename)
    elif filename in BROKEN_FILES_2:
        print("Removing file: " + filename)
    elif filename in BAD_FILES:
        print("Removing file: " + filename)
    else:
        print("Keeping file: " + filename)
        src = DIR_INPUT + "/" + filename
        dst = DIR_OUTPUT + "/" + filename
        shutil.copyfile(src, dst)

# run main 
if __name__=="__main__":
    main()