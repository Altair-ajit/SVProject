import pandas as pd
from pandas import DataFrame as df
from scipy import stats
import numpy as npp

def getBMIppl():
    files = "subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    runNumbers = []
    for row in range(pplFile.shape[0]):
        if not pd.isna(pplFile.iloc[row][3]):
            runNumbers.append(pplFile.iloc[row][2])
    return runNumbers

def getAgeppl():
    files = "subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    runNumbers = []
    for row in range(pplFile.shape[0]):
        if not pd.isna(pplFile.iloc[row][4]):
            runNumbers.append(pplFile.iloc[row][2])
    return runNumbers

def getBMI(x):
    files = "subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    for row in range(pplFile.shape[0]):
        if pplFile.iloc[row][2] == x:
            return pplFile.iloc[row][3]
    return null

def getAge(x):
    files = "subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    for row in range(pplFile.shape[0]):
        if pplFile.iloc[row][2] == x:
            return pplFile.iloc[row][4]
    return null

    



