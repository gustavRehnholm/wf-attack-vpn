'''
Analyze the extracted dataset

Application names in use (extracted from get_keywords.py)
['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
headers:
['connection', 'timestamps', 'sizes', 'directions', 'file_names']

touch stdout/extract_dataset_analysis.txt
wf-attack-vpn/extract_dataset_analysis.py | tee extract_dataset_analysis.txt
'''
import pandas as pd

def main(): 
    YOUTUBE_INDEX = 0
    SFTP_INDEX    = 1
    SKYPE_INDEX   = 2
    SSH_INDEX     = 3
    RDP_INDEX     = 4
    RSYNC_INDEX   = 5
    VOIP_INDEX    = 6
    SCP_INDEX     = 7
    NETFLIX_INDEX = 8
    VIMEO_INDEX   = 9

    APPLICATIONS = ['youtube', 'sftp', 'skype-chat', 'ssh', 'rdp', 'rsync', 'voip', 'scp', 'netflix', 'vimeo']
    duration_list = []

    # analyse each application
    for i in range(0, len(APPLICATIONS)):
        df = pd.read_hdf(APPLICATIONS[i] + ".h5")

        print("--------------------------------------------------------------")
        print(APPLICATIONS[i])
        print("Number of captures: " + str(df.shape[0]))

        times          = df["timestamps"].to_list()
        all_timestamps = []
        duration       = 0

        for list_times in times:
            #list_times.sort()
            #print("this duration")
            #print(list_times[-1] - list_times[0])
            duration += list_times[-1] - list_times[0]
            for item in list_times:
                if not isinstance(item, float):
                    print("ERROR: time is not a float")
                    print("Aborting the program")
                    return
                else:
                    all_timestamps.append(item)

        all_timestamps.sort()

        duration_list.append(duration)

        hours = duration / (60 * 60)
        print("")
        print("the number of packets: " + str(len(all_timestamps)))
        print("the duration(sec): " + str(duration))
        print("the duration(h): " + str(hours))


    # The relevant durations in hours
    total_duration         = sum(duration_list) / (60 * 60) 
    streaming_duration     = (duration_list[0] + duration_list[8] + duration_list[9]) / (60 * 60)
    chat_duration          = duration_list[2] / (60 * 60)
    c2_duration            = (duration_list[3] + duration_list[4] ) / (60 * 60)
    file_transfer_duration = (duration_list[1] + duration_list[5] + duration_list[7] ) / (60 * 60)
    voip_duration          = duration_list[6] / (60 * 60)

    print("")
    print("--------------------------------------------------------------")
    print("Streaming VPN noise(h): " + str(streaming_duration))
    print("Chat VPN noise(h): " + str(chat_duration))
    print("c2 VPN noise(h): " + str(c2_duration))
    print("file transfer VPN noise(h): " + str(file_transfer_duration))
    print("voip VPN noise(h): " + str(voip_duration))
    print("")
    print("Total VPN noise(h): " + str(total_duration))
    print("--------------------------------------------------------------")
    print("How large part the different noises are:")
    print("")
    print("Streaming: " + str(streaming_duration / total_duration))
    print("Chat: " + str(chat_duration / total_duration))
    print("c2: " + str(c2_duration / total_duration))
    print("file transfer: " + str(file_transfer_duration / total_duration))
    print("voip: " + str(voip_duration / total_duration))
        

if __name__=="__main__":
    main()