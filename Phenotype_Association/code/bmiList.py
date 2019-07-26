import pandas as pd
from pandas import DataFrame as df
from scipy import stats
import numpy as npp
from Bio import Entrez
from bs4 import BeautifulSoup as BS
import lxml    


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
    Entrez.email = 'rajitzp@gmail.com'
    handle = Entrez.efetch('taxonomy', id=x, rettype='xml')
    response = Entrez.read(handle)
    sci_names = []
    for entry in response:
         sci_names.append(entry.get('ScientificName'))
    return sci_names
    
    

def parseName(x):
    regionscount = 1
    counting = True
    counting2 = False
    taxID = ""
    bins = ""
    for count in range(len(x)):
        if x[count] == "." and counting:
            counting = False
        if x[count] == ":" and not counting:
            counting2 = True
        if counting:
            taxID += x[count]
        if counting2:
            bins += x[count]
            if x[count] == ";":
                regionscount += 1
    if regionscount > 2:
        bins = ":" + str(regionscount) + " regions"
    return taxID, bins
        

        


    



