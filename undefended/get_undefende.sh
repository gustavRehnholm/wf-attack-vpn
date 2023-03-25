#!/bin/bash

# 10-fold on the undefended dataset

./df-fitness.py -d foreground_traffic/client --train -s 100 -f 1 --csv merged_traffic/undef/fold1.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 2 --csv merged_traffic/undef/fold2.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 3 --csv merged_traffic/undef/fold3.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 4 --csv merged_traffic/undef/fold4.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 5 --csv merged_traffic/undef/fold5.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 6 --csv merged_traffic/undef/fold6.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 7 --csv merged_traffic/undef/fold7.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 8 --csv merged_traffic/undef/fold8.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 9 --csv merged_traffic/undef/fold9.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 0 --csv mermerged_trafficged/undef/fold0.csv