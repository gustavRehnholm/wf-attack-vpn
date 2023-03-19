#!/bin/bash

# ./wf-attack-vpn/wf-attack/wf-attack.sh

# ittr-no offset
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_no_offset/twitch_no_offset_2600h wf-result/twitch/twitch_no_offset/twitch_no_offset_2600h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_no_offset/twitch_no_offset_5h wf-result/twitch/twitch_no_offset/twitch_no_offset_5h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_no_offset/twitch_no_offset_2_5h wf-result/twitch/twitch_no_offset/twitch_no_offset_2.5h

# ittr-offset
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_offset/twitch_offset_2600h wf-result/twitch/twitch_no_offset/twitch_no_offset_2600h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_offset/twitch_offset_5h    wf-result/twitch/twitch_no_offset/twitch_no_offset_5h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_offset/twitch_offset_2_5h  wf-result/twitch/twitch_no_offset/twitch_no_offset_2.5h

# rnd-no offset
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2600h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_5h    wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_5h
#python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h  wf-result/twitch/twitch_rnd_no_offset/twitch_rnd_no_offset_2_5h

# rnd-offset
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2600h wf-result/twitch_rnd_offset/twitch_rnd_offset_2600h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_5h    wf-result/twitch_rnd_offset/twitch_rnd_offset_5h
python wf-attack-vpn/wf-attack/wf-attack-dir.py merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2_5h  wf-result/twitch_rnd_offset/twitch_rnd_offset_2_5h

# divide
# divide-rnd


# rnd with offset
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2600h 1    True True False
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_offset/twitch_rnd_offset_5h    500  True True False
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_rnd_offset/twitch_rnd_offset_2_5h  1000 True True False

# divide without rnd
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_2600h 1    True False True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_5h    500  True False True
python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_ittr/twitch_div_ittr_2_5h  1000 True False True

# divide with rnd
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_rnd/twitch_div_rnd_2600h 1    True True True
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_rnd/twitch_div_rnd_5h    500  True True True
#python wf-attack-vpn/generate_merged_dataset/main.py foreground_traffic background_traffic/twitch.h5 merged_traffic/twitch_div_rnd/twitch_div_rnd_2_5h  1000 True True True

