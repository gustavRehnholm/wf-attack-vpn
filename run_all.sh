#!/bin/bash

# ./wf-attack-vpn/run_all.sh

./wf-attack-vpn/generate_merged_dataset/run_all.sh

./wf-attack-vpn/wf-attack/wf-attack.sh

./wf-attack-vpn/plotter/plot.sh