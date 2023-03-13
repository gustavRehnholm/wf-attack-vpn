
# merged_traffic/twitch_offset_30_60_0 
# wf-result/twitch_offset_30_60_0/twitch_tiktok.csv

# merged_traffic/twitch_small_offset_30_60_0 
# wf-result/twitch_small_offset_30_60_0/twitch_tiktok.csv

# merged_traffic/twitch_smallest_offset_30_60_0 
# wf-result/twitch_small_offset_30_60_0/twitch_tiktok.csv

./df-fitness.py -d merged_traffic/twitch_small_offset_30_60_0 --train --csv wf-result/twitch_small_offset_30_60_0/twitch_default.csv

./df-fitness.py -d merged_traffic/twitch_small_offset_30_60_0 --train --constant --csv wf-result/twitch_small_offset_30_60_0/twitch_constant.csv

./df-fitness.py -d merged_traffic/twitch_small_offset_30_60_0 --train --tiktok --csv wf-result/twitch_small_offset_30_60_0/twitch_tiktok.csv