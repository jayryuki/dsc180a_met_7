from os import listdir
from os.path import isfile, join
import os
import pandas as pd

def test_data(datadir, outdir, evaluatedir):
    report = open(r'test_report.txt', 'w+')
    for file in os.listdir(datadir):
        current = os.path.join(datadir, file)
        print(current)