import pandas as pd
from pandas import DataFrame as df
from scipy import stats
import numpy as npp



def getBMIppl():
    files = "../data/subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    runNumbers = []
    for row in range(pplFile.shape[0]):
        if not pd.isna(pplFile.iloc[row][3]):
            runNumbers.append(pplFile.iloc[row][2])
    return runNumbers

def getAgeppl():
    files = "../data/subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    runNumbers = []
    for row in range(pplFile.shape[0]):
        if not pd.isna(pplFile.iloc[row][4]):
            runNumbers.append(pplFile.iloc[row][2])
    return runNumbers

def getBMI(x):
    files = "../data/subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    for row in range(pplFile.shape[0]):
        if pplFile.iloc[row][2] == x:
            return pplFile.iloc[row][3]
    return null

def getAge(x):
    files = "../data/subset_ena2fd.csv"
    pplFile = pd.read_csv(files)
    for row in range(pplFile.shape[0]):
        if pplFile.iloc[row][2] == x:
            return pplFile.iloc[row][4]
    return null

def getTax(x):
    files = "../data/refseq-genbank.csv"
    refFile = pd.read_csv(files)
    for row in range(refFile.shape[0]):
        if x == refFile.iloc[row][0] or x == refFile.iloc[row][1]:
            return refFile.iloc[row][2]
    return "Null"

def parseName(x):
    start = 0
    finalstr = ""
    for num in range(len(x)):
        if x[num] == "P" and start < 1:
            start += 1
            finalstr += x[num]
        elif not x[num].isdigit() and start >= 1:
            num = len(x)
        else:
            finalstr += x[num]
    return finalstr
        

        


    



