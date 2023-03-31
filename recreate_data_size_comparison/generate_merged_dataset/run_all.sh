#!/bin/bash
# {foreground} {background} {merged} {size} {offset} {rnd} {divide}

# ./wf-attack-vpn/generate_merged_dataset/run_all.sh

# ittr with offset
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_ittr_offset/twitch_ittr_offset_2600h 1    True False False
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_ittr_offset/twitch_ittr_offset_2_5h  1000 True False False

# divide without rnd
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_2600h 1    True False True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_2_5h  1000 True False True