'''
Go though all twitch captures, and store them parsed as h5 files (containing dataframe)
But will only use files that are of good enough quality

touch stdout/merge_parsed_noise.txt
python wf-attack-vpn/KAU-twitch-parsing/merge_parsed_noise.py | tee stdout/merge_parsed_noise.txt
'''

import pandas as pd
import os

def main():
    # parsed noise files
    DIR_NOISE = "twitch/parsed_captures/"
    # the merged noise file in teh h5 format
    DIR_MERGED_NOISE = "twitch/merged_captures/"

    COL_NAMES =  ['timeframe', 'direction', 'size']

    time_deviation = 0
    merged_df = pd.DataFrame(columns = COL_NAMES)

    for file in os.listdir(DIR_NOISE):
        filename = os.fsdecode(file)

        if not filename.endswith(".log"): 
            print("ERROR: the file (" + str(filename) + ") should not be part of the directory")
            print("Only log files should be part of the twitch dataset")
            print("Aborting the program")
            return

        path = DIR_NOISE + filename
        df_file = pd.read_csv(path, names = COL_NAMES)

        print(df_file.keys())

        return

        '''
        # time corrections on the timeframes
        for i, row in df.iterrows():
            row["timeframe"] =  row["timeframe"] + deviation_time

        # to shift each new capture forward in time
        time_deviation = df['timeframe'].iloc[-1]

        
        merged_df = pd.concat([merged_df, df_file], axis=0)

    # Store the result in h5 file, for future use of the data
    df_file_name = DIR_PARSED_NOISE + "twitch.h5" 
    merged_df.to_hdf(df_file_name, mode = "w", key = "df")
    '''

# run main 
if __name__=="__main__":
    main()