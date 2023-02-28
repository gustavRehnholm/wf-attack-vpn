import pandas as pd

'''
extract the captured VPN data that has been generated from the MIT project
and create new dataframes, stored in h5 format, after teh application used.
All data that has been captured with non vpn traffic, will be removed.

Application names in use (extracted from get_keywords.py)
['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
headers:
['connection', 'timestamps', 'sizes', 'directions', 'file_names']
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
        dataframe_list.append(pd.DataFrame( columns = df.columns.values.tolist()))

    # Read whole dataset from MIT
    nr_of_rows = 0
    nr_of_vpn = 0
    nr_of_nonvpn = 0
    nr_of_app = [0] * len(APPLICATIONS)

    for index, row in df.iterrows():
        nr_of_rows += 1
        fileType = row['file_names'].split("_")
        vpn = fileType[0]
        application = fileType[1]

        # Skip all captured data that are not VPN traffic
        if vpn == "nonvpn":
            nr_of_nonvpn += 1
            continue
        # Store vpn traffic
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

    print("total rows in the dataset: " + str(nr_of_rows))
    print("VPN rows in the dataset: " + str(nr_of_vpn)) 
    print("NON-VPN rows in the dataset: " + str(nr_of_nonvpn))
    print("number of rows per application")
    for i in range(0, len(nr_of_app)):
        print(str(APPLICATIONS[i]) + " : " + str(nr_of_app[i]))

    # to csv (for testing)
    for i in range(0, len(dataframe_list)):
        df_file_name = APPLICATIONS[i] + ".csv"
        dataframe_list[i].to_csv(df_file_name, index = True)

    # Store the result in h5 file, for the parser
    for i in range(0, len(dataframe_list)):
        df_file_name = APPLICATIONS[i] + ".h5"
        dataframe_list[i].to_hdf(df_file_name, mode = "w", key = "df")


if __name__=="__main__":
    main()