#!/usr/bin/python3

'''
Get the keywords that exits in the MIT dataset, which is:
['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
'''

import pandas as pd

def get_keywords(h5_file): 
    df = pd.read_hdf(h5_file)

    filenames = df['file_names'].tolist()

    for i in range(0, len(filenames)):
        filenames[i] = filenames[i].split("_")[1]

    unique_filenames = list(dict.fromkeys(filenames))
    return unique_filenames