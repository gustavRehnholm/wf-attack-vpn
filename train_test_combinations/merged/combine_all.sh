#!/bin/bash
# To create all the combinations on how to to test the attacker with access to other background dataset

# to run:
# ./wf-attack-vpn/train_test_combinations/merged/combine_all.sh

# structure deestination merged_traffic/combined/<train set>/<test set>/<fold>

# test streaming against eachother
#python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/mit_5k/vimeo --test merged_traffic/mit_5k/netflix --title vimeo_netflix
#python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/mit_5k/vimeo --test merged_traffic/mit_5k/youtube --title vimeo_youtube

#python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py      --train merged_traffic/mit_5k/netflix --test merged_traffic/mit_5k/vimeo   --title netflix_vimeo
#python wf-attack-vpn/train_test_combinations/unmergeddef/combine_datasets.py --train merged_traffic/mit_5k/netflix --test merged_traffic/mit_5k/youtube --title netflix_youtube

#python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/mit_5k/youtube --test merged_traffic/mit_5k/netflix --title youbute_netflix       
#python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/mit_5k/youtube --test merged_traffic/mit_5k/vimeo   --title youbute_vimeo

# test recorded streaming against 
python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/twitch_div_rnd_1_middle --test merged_traffic/mit_5k/netflix --title twitch_netflix
python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/twitch_div_rnd_1_middle --test merged_traffic/mit_5k/vimeo   --title twitch_vimeo
python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/twitch_div_rnd_1_middle --test merged_traffic/mit_5k/youtube --title twitch_youbute

python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/mit_5k/netflix  --test merged_traffic/twitch_div_rnd_1_middle --title netflix_twitch
python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/mit_5k/vimeo    --test merged_traffic/twitch_div_rnd_1_middle --title vimeo_twitch
python wf-attack-vpn/train_test_combinations/merged/combine_datasets.py --train merged_traffic/mit_5k/youtube  --test merged_traffic/twitch_div_rnd_1_middle --title youtube_twitch

python wf-attack-vpn/plot_graphs/plot_all.py -r wf_result/combined_merged_print -w 10 -g fig/combined_merged