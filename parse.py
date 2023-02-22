import pandas as pd

'''

'''

def main(): 
    df = pd.read_hdf("VNAT_Dataframe_release_1.h5")

    print(df)

if __name__=="__main__":
    main()