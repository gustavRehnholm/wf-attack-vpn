#!/bin/bash
# ./wf-attack-vpn/Parse_noise/KAU-twitch-parsing/run_all.sh

# All steps to go from the raw captures, to noise that one can merge with the web traffic

# convert the log files the dataframes, and store them as h5 files
python wf-attack-vpn/parse_background/KAU-twitch-parsing/log_2_h5.py

# rm the capture files that are broken 
python wf-attack-vpn/parse_background/KAU-twitch-parsing/rm_broken_captures.py

# Parse the noise, which is now stored as dataframes  in h5 files
python wf-attack-vpn/parse_background/KAU-twitch-parsing/parse.py

python wf-attack-vpn/parse_background/KAU-twitch-parsing/merge_parsed_noise.py