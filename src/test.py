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

    os.system('mkdir -p ' + test_resultsdir)
    os.system('mkdir -p ' + metricsdir)
    os.system('mkdir -p ' + plotsdir)
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    os.system("python" + " " + ate + " " + slam + " " + gt + " " +  "--plot ate.png")
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    print(output)
    os.system("python" + " " + rpe + " " + odom + " " + gt + " " +  "--plot rpe.png --fixed_delta > ate_ouput.txt")

    os.system('mv ate.png ' + plotsdir)
    os.system('mv rpe.png ' + plotsdir)

    #os.system('mv )"outdir":"results/",=