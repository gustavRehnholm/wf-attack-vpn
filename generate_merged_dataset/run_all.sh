#!/bin/bash
# {foreground} {background} {merged} {size} {offset} {rnd}

# ./wf-attack-vpn/generate_merged_dataset/run_all.sh


# rnd no offset
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h 1
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    500
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  1000

# rnd with offset
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h 1    True True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    500  True True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  1000 True True