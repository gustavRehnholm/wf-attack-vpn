#!/usr/bin/python3

import pandas as pd

'''
To run:
python wf-attack-vpn/parse_background/MIT-h5-parsing/extract_dataset.py
'''

def main():
    extract_dataset()
    return

def extract_dataset(): 
    '''
    extract the captured VPN data that has been generated from the MIT project
    and create new dataframes, stored in h5 format, after the application used.
    All data that has been captured with non vpn traffic, will be skipped.
    The data is not parsed.

    Application names in use (extracted from get_keywords.py)
    ['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
    headers:
    ['connection', 'timestamps', 'sizes', 'directions', 'file_names']
    '''
    
    INPUT_FILE = "mit/VNAT_Dataframe_release_1.h5"
    # the whole dataset
    df = pd.read_hdf(INPUT_FILE)

    # The applications that the dataset have
    #APPLICATIONS = ['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
    APPLICATIONS = get_keywords(INPUT_FILE)
    # where to store the result
    DIR_RESULT = "mit/raw_applications"

    os.system("mkdir " + DIR_RESULT)

    # One dataframe for each application, with the correct headers
    dataframe_list = []
    for i in range(0, len(APPLICATIONS)):
        dataframe_list.append(pd.DataFrame( columns = df.columns.values.tolist()))

    # information about the dataset as a whole
    # number of captures in total, that are vpn and that are not vpn traffic
    nr_of_rows   = 0
    nr_of_vpn    = 0
    nr_of_nonvpn = 0
    # number of vpn captures per application
    nr_of_app    = [0] * len(APPLICATIONS)

    # Read whole dataset from MIT
    for index, row in df.iterrows():
        nr_of_rows += 1

        # the capture vpn and application type
        fileType    = row['file_names'].split("_")
        vpn         = fileType[0]
        application = fileType[1]


        if vpn == "nonvpn":
            nr_of_nonvpn += 1
            continue
        # Store vpn traffic in the right dataframe
        elif vpn == "vpn":
            nr_of_vpn += 1
            for i in range(0, len(APPLICATIONS)):
                if application == APPLICATIONS[i]:
                    dataframe_list[i].loc[len(dataframe_list[i])] = row
                    nr_of_app[i] += 1
        else:
            print("ERROR: one file name did not start with vpn or nonvpn, but: ", vpn)
            print("Aborting program")
            return

    print("")
    print("---------------------------------------------")
    print("total rows in the dataset: " + str(nr_of_rows))
    print("VPN rows in the dataset: " + str(nr_of_vpn)) 
    print("NON-VPN rows in the dataset: " + str(nr_of_nonvpn))
    print("")
    print("number of rows per application")
    for i in range(0, len(nr_of_app)):
        print(str(APPLICATIONS[i]) + " : " + str(nr_of_app[i]))
    print("")

    # Store the result in h5 file, for future use of the data
    for i in range(0, len(dataframe_list)):
        df_file_name = "h5/" + APPLICATIONS[i] + ".h5"
        dataframe_list[i].to_hdf(df_file_name, mode = "w", key = "df")


def get_keywords(h5_file): 
    '''
    Get the keywords that exits in the MIT dataset, which is:
    ['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
    Args:
        h5_file - Required : Path to the hdf5 file to get the keywords for (str)
    Return:
        list of keywords (List[str])
    '''
    df = pd.read_hdf(h5_file)

    filenames = df['file_names'].tolist()

    for i in range(0, len(filenames)):
        filenames[i] = filenames[i].split("_")[1]

    unique_filenames = list(dict.fromkeys(filenames))
    return unique_filenames

if __name__=="__main__":
    main()