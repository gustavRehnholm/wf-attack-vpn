#!/usr/bin/expect

set timeout -1

spawn ./wf-attack-vpn/plotter/plot_all.py

expect "Where is the csv files located?"

send -- "wf-result/twitch/no_offset"

