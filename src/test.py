from os import listdir
from os.path import isfile, join
import os
import pandas as pd
import sys

def test_data(datadir, test_resultsdir, metricsdir, plotsdir, ate, rpe):
    report = open(r'test_report.txt', 'w+')
    slam = ''
    odom = ''
    gt = ''

    os.system('mkdir -p ' + test_resultsdir)
    os.system('mkdir -p ' + metricsdir)
    os.system('mkdir -p ' + plotsdir)
    counter = 0
    for folders in os.listdir(datadir):
        current_folder = os.path.join(datadir, folders)
        for file in os.listdir(current_folder):
            current = os.path.join(current_folder, file)

            if 'slam' in current:
                slam += current
            
            if 'odom' in current:
                odom += current
            
            if 'gt' in current:
                gt += current


        ate = os.popen('python' + ' ' + ate + ' ' + slam + ' ' + gt + ' ' +  '--plot ate_' + counter + '.png').read()
        rpe = os.popen('python' + ' ' + rpe + ' ' + odom + ' ' + gt + ' ' +  '--plot rpe_' + counter + '.png --fixed_delta').read()

        print('ahahahah')
        print(ate)
        print(rpe)
        os.system('mv ate_' + counter + plotsdir)
        os.system('mv rpe_' + counter + plotsdir)

        counter += 1

    #os.system('mv )"outdir":"results/",=