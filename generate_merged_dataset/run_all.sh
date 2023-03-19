#!/bin/bash
# {foreground} {background} {merged} {size} {offset} {rnd} {divide}

# ./wf-attack-vpn/generate_merged_dataset/run_all.sh

# ittr without offset

# ittr with offset

# rnd no offset
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h 1    False True False
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    500  False True False
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  1000 False True False

# rnd with offset
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2600h 1    True True False
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_offset/twitch_rnd_offset_5h    500  True True False
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2_5h  1000 True True False

# divide without rnd
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_2600h 1    True False True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_5h    500  True False True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_2_5h  1000 True False True

# divide with rnd
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_rnd/twitch_div_rnd_2600h 1    True True True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_rnd/twitch_div_rnd_5h    500  True True True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_rnd/twitch_div_rnd_2_5h  1000 True True True