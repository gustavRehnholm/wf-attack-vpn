import pandas as pd

'''
extract the captured VPN data that has been generated from the MIT project

python wf-attack-vpn/extract_captures.py
'''

def main(): 
    df = pd.read_hdf("VNAT_Dataframe_release_1.h5")

    print("The DataFrame :")
    print(df)


    print("The column headers :")
    print(df.columns.tolist())

if __name__=="__main__":
    main()