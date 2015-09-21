#!/bin/sh
python3 ~/twscan/scan.py ~/twscan/capture1.txt > map.dot
neato -Tpdf map.dot > map.pdf
