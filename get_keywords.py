import pandas as pd

'''
Get the keywords that exits in the data, which is:

['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']

python wf-attack-vpn/get_keywords.py
'''

def main(): 
    df = pd.read_hdf("VNAT_Dataframe_release_1.h5")

    filenames = df['file_names'].tolist()

    for i in range(0, len(filenames)):
        filenames[i] = filenames[i].split("_")[1]

    unique_filenames = list(dict.fromkeys(filenames))
    print(unique_filenames)

if __name__=="__main__":
    main()