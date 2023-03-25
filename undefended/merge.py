#!/usr/bin/env python3
#!/usr/bin/env python3
import pandas as pd

'''
merge the 10 fold, so it can be showed as one graph
'''
def main():
    key = "df"
    PATH_OUTPUT_H5 = "merged_traffic/undef/combined.h5"
    PATH_OUTPUT_CSV = "merged_traffic/undef/combined.csv"
    list_of_csv = os.listdir("merged_traffic/undef")
   
    for csv_file in list_of_csv:
        df = pd.read_csv(csv_file)
        df.to_hdf(PATH_OUTPUT_H5, mode = "r+", key = key, append = True)

    # hdf5 to dataframe
    df = pd.read_hdf(PATH_OUTPUT_H5, key=key)
    # dataframe to csv
    df.to_csv(PATH_OUTPUT_CSV, index = False)
    # rm hdf5
    os.system("rm "+ PATH_OUTPUT_H5)

# run main 
if __name__=="__main__":
    main()