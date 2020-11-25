from os import listdir
from os.path import isfile, join
import os
import pandas as pd
import sys

def test_data(datadir, outdir, ate, rpe):
    report = open(r'test_report.txt', 'w+')
    slam = ''
    odom = ''
    gt = ''
    for file in os.listdir(datadir):
        current = os.path.join(datadir, file)
        if 'slam' in current:
            slam += current
        
        if 'odom' in current:
            odom += current
        
        if 'gt' in current:
            gt += current


    print(slam)
    print(odom)
    print(gt)
    print("python" + " " + slam + " " + gt + " " + "--plot ate.pdf")
    os.system("python" + " " + ate + " " + slam + " " + gt + " " +  "--plot " + outdir + "ate.png")
        