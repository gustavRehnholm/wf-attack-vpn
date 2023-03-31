#!/bin/bash

# 10-fold on the undefended dataset
# ./wf-attack-vpn/undefended/get_undefended.sh

./df-fitness.py -d foreground_traffic/client --train -s 100 -f 1 --csv wf-result/undef/10-fold/fold1.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 2 --csv wf-result/undef/10-fold/fold2.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 3 --csv wf-result/undef/10-fold/fold3.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 4 --csv wf-result/undef/10-fold/fold4.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 5 --csv wf-result/undef/10-fold/fold5.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 6 --csv wf-result/undef/10-fold/fold6.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 7 --csv wf-result/undef/10-fold/fold7.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 8 --csv wf-result/undef/10-fold/fold8.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 9 --csv wf-result/undef/10-fold/fold9.csv
./df-fitness.py -d foreground_traffic/client --train -s 100 -f 0 --csv wf-result/undef/10-fold/fold0.csv

python wf-attack-vpn/k-fold/fold_mean.py

python wf-attack-vpn/plotter/plot_all.py undefended wf-result/undef/10-fold fig/undef