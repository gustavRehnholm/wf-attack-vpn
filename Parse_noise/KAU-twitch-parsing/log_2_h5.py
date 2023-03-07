#!/usr/bin/python3

'''
Convert the raw log files to dataframes, and store them with h5
That way, they will be faster to handle

touch stdout/log_2_h5.txt
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/log_2_h5.py | tee stdout/log_2_h5.txt
'''

import pandas as pd
import os

def main():
    print("Start converting twitch traffic")
    # parsed noise files
    DIR_INPUT = "captures/"
    # the captures in h5 format
    DIR_OUTPUT = "twitch/raw_captures_h5/"

    COL_NAMES =  ['time', 'sender_receiver', 'size']

    # clean the previous result
    os.system("rm -f -r " + DIR_OUTPUT)
    os.system("mkdir " + DIR_OUTPUT)


    index = 0
    for file in os.listdir(DIR_INPUT):

        filename = os.fsdecode(file)
        if not filename.endswith(".log"): 
            print("ERROR: the file (" + str(filename) + ") should not be part of the directory")
            print("Only log files should be part of the twitch dataset")
            print("Aborting the program")
            return

        index += 1
        print("")
        print("converting file " + str(index) + "/1370: " + str(filename))
        print("")

        path = DIR_INPUT + filename
        df = pd.read_csv(path, names = COL_NAMES, delim_whitespace = True)

        df_file_name = DIR_OUTPUT + filename.rsplit('.', 1)[0] + '.h5'
        df.to_hdf(df_file_name, mode = "w", key = "df")

# run main 
if __name__=="__main__":
    main()