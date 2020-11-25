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
    for folders in os.listdir(datadir):
        current_folder = os.path.join(datadir, folders)
        for file in os.listdir(current_folder):
            current = os.path.join(current_folder, file)

            if 'slam' in current:
                print('Slam is now: ' + current)
                slam += current
            
            if 'odom' in current:
                print('Odom is now: ' + current)
                odom += current
            
            if 'gt' in current:
                print('GT is now: ' + current)
                gt += current

    os.system('mkdir -p ' + outdir + 'test_results')
    os.system('mkdir -p ' + outdir + 'metrics')
    os.system('mkdir -p ' + outdir + 'plots')

    os.system("python" + " " + ate + " " + slam + " " + gt + " " +  "--plot ate.png > ate_ouput.txt")
    os.system("python" + " " + rpe + " " + odom + " " + gt + " " +  "--plot rpe.png --fixed_delta > rpe_ouput.txt")

    os.system('mv ate.png ' + plotsdir)
    os.system('mv rpe.png ' + plotsdir)