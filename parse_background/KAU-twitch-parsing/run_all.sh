#!/bin/bash
# ./wf-attack-vpn/Parse_noise/KAU-twitch-parsing/run_all.sh

# All steps to go from the raw captures, to noise that one can merge with the web traffic

# convert the log files the dataframes, and store them as h5 files
touch stdout/log_2_h5.txt
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/log_2_h5.py | tee stdout/log_2_h5.txt

# rm the capture files that are broken 
touch stdout/rm_broken_captures.txt
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/rm_broken_captures.py | tee stdout/rm_broken_captures.txt


# Parse the noise, which is now stored as dataframes  in h5 files
touch stdout/parse.py
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/parse.py | tee stdout/parse.py

# merge all the captures the one large noise file
touch stdout/merge_parsed_noise.py
python wf-attack-vpn/Parse_noise/KAU-twitch-parsing/merge_parsed_noise.py | tee stdout/merge_parsed_noise.py