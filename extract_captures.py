import pandas as pd

'''
extract the captured VPN data that has been generated from the MIT project
and create new dataframes, stored in h5 format, after teh application used.
All data that has been captured with non vpn traffic, will be removed.

Application names in use (extracted from get_keywords.py)
['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
'''

# Extract all data that are from VPN traffic, and store them in different dataframes depending on the application
def main(): 
    # the whole dataset
    df = pd.read_hdf("VNAT_Dataframe_release_1.h5")

    # The applications that the dataset have
    APPLICATIONS = ['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']

    # One dataframe for each application
    dataframe_list = []
    for i in range(0, len(APPLICATIONS)):
        dataframe_list.append(pd.DataFrame())

    # Read whole dataset from MIT
    for index, row in df.iterrows():
        fileName = row['file_names']
        fileType = fileName.split("_")
        vpn = fileType[0]
        application = fileType[1]

        # Skip all captured data that are not VPN traffic
        if vpn == "nonvpn":
            continue
        # Store vpn traffic
        elif vpn == "vpn":
            for i in range(0,APPLICATIONS):
                if application == APPLICATIONS[i]:
                    dataframe_list[i].append(row)
        else:
            print("ERROR: one file name did not start with vpn or nonvpn, but: ", vpn)
            print("Aborting program")
            return

    # to csv (for testing)
    for i, dataframe in dataframe_list:
        df_file_name = APPLICATIONS[i] + ".csv"
        dataframe.to_csv(df_file_name, index = True)

    # Store the result in h5 file, for the parser
    for i, dataframe in dataframe_list:
        df_file_name = APPLICATIONS[i] + ".h5"
        dataframe.to_hdf(df_file_name, mode = "w")


if __name__=="__main__":
    main()