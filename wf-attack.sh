
# merged_traffic/twitch_offset_30_60_0
# merged_traffic/twitch_small_offset_30_60_0

./df-fitness.py -d merged_traffic/twitch_offset_30_60_0/ --train --csv wf-result/twitch_default.csv

./df-fitness.py -d merged_traffic/twitch_offset_30_60_0/ --train --constant --csv wf-result/twitch_constant.csv

./df-fitness.py -d merged_traffic/twitch_offset_30_60_0/ --train --tiktok --csv wf-result/twitch_tiktok.csv