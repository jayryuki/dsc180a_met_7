from os import listdir
from os.path import isfile, join
import os
import pandas as pd
import sys

def test_data(datadir, outdir, plotsdir, ate, rpe):
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


    print('mkdir -p ' + outdir + '/{test_results, plots, metrics}')
    os.system('mkdir -p ' + outdir + '/{test_results, plots, metrics}')
  
    os.system("python" + " " + ate + " " + slam + " " + gt + " " +  "--plot ate.png > ate_ouput.txt")
    os.system("python" + " " + rpe + " " + odom + " " + gt + " " +  "--plot rpe.png --fixed_delta > rpe_ouput.txt")


    #os.system('mkdir -p results/metrics')
    os.system('mv ate.png ' + plotsdir)
    os.system('mv rpe.png ' + plotsdir)