import pandas as pd
import random

BACKGROUND_FILE = "~/Downloads/twitch_1.h5"
BACKGROUND_DIR = "/home/pulls/dataset/dataset-Maybenot-Firefox-WireGuard-2021-Week-15"

def main():
    print("reading background data")
    background = pd.read_hdf(BACKGROUND_FILE, key = "df")
    print(background.head(10))

    minutes = background["time"].sum() / (1000000000*60)
    print("total time: ", minutes, " minutes")
    
    print(f"we split 8:1:1, based on time, where background has index [0,{len(background)-1}]")
    total_time = background["time"].sum()
    training_end_index = background["time"].cumsum().searchsorted(total_time * 0.8) - 1
    validation_end_index = background["time"].cumsum().searchsorted(total_time * 0.9) - 1
    print(f"\ttraining range [0,{training_end_index}]")
    print(f"\tvalidation range [{training_end_index}, {validation_end_index}]")
    print(f"\ttesting range [{validation_end_index} to {len(background)-1}]")

    print("reading fold csv")
    fold = pd.read_csv(f"{BACKGROUND_DIR}/fold-0.csv")
    print(fold.head(10))

    def merge(foreground, background):
        # merge the foreground and background
        print(foreground.head(10))
        print(background.head(10))

        # iterate over each row in the foreground, read the log
        # and merge it with the background
        for index, row in foreground.iterrows():
            fname = f"{BACKGROUND_DIR}/client/{row['log']}"
            print(fname)

            # generate a random starting index in the background
            b_index = random.randint(0, len(background)-1)

            merged = ""

            # read the foreground log as a string into memory
            with open(fname, "r") as f:
                lines = f.readlines()

                last_time = 0
                # iterate over each line in the foreground log
                for line in lines:
                    # get the time
                    time, _ = line.split(",", 1)

                    if len(merged) == 0:
                        # if this is the first line, just add it
                        merged += line
                        last_time = int(time)
                        continue
                    
                    # add background packets until the time until the next foreground packet
                    # is smaller than the time until the next background packet
                    while background.iat[b_index, 0] < int(time) - last_time:
                        merged += f"{background.iat[b_index, 0] + last_time},{background.iat[b_index, 1]}b,{background.iat[b_index, 2]}\n"
                        last_time += int(background.iat[b_index, 0])

                        b_index += 1
                        if b_index >= len(background):
                            b_index = 0
                    
                    # add the foreground packet
                    merged += line
                    last_time = int(time)

            # write the merged log to a file
            with open(f"{BACKGROUND_DIR}/merged/{row['log']}", "w") as f:
                f.write(merged)
    
    print("merging training data")
    merge(fold[fold['is_train'] == True], background[:training_end_index])
    print("merging validation data")
    merge(fold[fold['is_valid'] == True], background[training_end_index:validation_end_index])
    print("merging testing data")
    merge(fold[fold['is_test'] == True], background[validation_end_index:])
    print("done")

if __name__ == "__main__":
    main()