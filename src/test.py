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
            print(current)
            if 'slam' in current:
                slam += current
            
            if 'odom' in current:
                odom += current
            
            if 'gt' in current:
                gt += current


        ate = os.popen('python' + ' ' + ate + ' ' + slam + ' ' + gt + ' ' +  '--plot ate_' + str(counter) + '.png').read()
        rpe = os.popen('python' + ' ' + rpe + ' ' + odom + ' ' + gt + ' ' +  '--plot rpe_' + str(counter) + '.png --fixed_delta').read()

        report.write(ate + ' ' + rpe)
        os.system('mv ate_' + str(counter) + '.png ' + plotsdir)
        os.system('mv rpe_' + str(counter) + '.png ' + plotsdir)
        os.system('mv test_report.txt '+ test_resultsdir)
        counter += 1

    report.close()