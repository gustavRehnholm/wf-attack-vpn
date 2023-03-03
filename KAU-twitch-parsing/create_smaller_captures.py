'''
Script to delete captures, used to test how many captures that are needed

touch stdout/create_smaller_captures.txt
python wf-attack-vpn/KAU-twitch-parsing/merge_parsed_noise.py | tee stdout/create_smaller_captures.txt
'''

import os
from os import walk
from os import path
# to copy files
import shutil

def main():
    print("script starts\n")

    DIR_MERGED_NOISE = "twitch/merged_captures/"

    df = pd.read_hdf(DIR_MERGED_NOISE + "twitch.h5")

    nr_of_packets = df[df.columns[0]].count()

    # 600 captures
    df_half = df.head(int(nr_of_packets/2))
    # 300 captures
    df_quarter = df.head(int(nr_of_packets/4))
    # 200 captures
    df_eighth = df.head(int(nr_of_packets/8))

    # Store the splitted noise
    df_half.to_hdf(DIR_MERGED_NOISE + "twitch_half.h5", mode = "w", key = "df")
    df_quarter.to_hdf(DIR_MERGED_NOISE + "twitch_quarter.h5", mode = "w", key = "df")
    df_eighth.to_hdf(DIR_MERGED_NOISE + "twitch_eighth.h5", mode = "w", key = "df")

# run main
if __name__=="__main__":
    main()