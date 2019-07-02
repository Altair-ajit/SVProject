import pandas as pd
from pandas import DataFrame as df
from scipy import stats
import numpy as np
import statsmodels
import bmiList
from statsmodels.stats.multitest import multipletests as mpt

#initiating the file to be read
deletions = "../data/dsgv.df"
dfile = pd.read_pickle(deletions)

#mann whitney for the columns
ageppl = bmiList.getAgeppl()
bmippl = bmiList.getBMIppl()

bmiOrder = []
ageOrder = []

for rows in range(dfile.shape[0]):
    rname = dfile.index[rows]
    if dfile.index[rows] in bmippl:
        bmiOrder.append(bmiList.getBMI(rname))
    if dfile.index[rows] in ageppl:
        ageOrder.append(bmiList.getAge(rname))

bmiUs = []
bmiPvals = []

ageUs = []
agePvals = []


for column in range(dfile.shape[1]):
    bmiDelArray = []
    ageDelArray = []
    for rows in range(dfile.shape[0]):
        adding = dfile.iloc[rows][dfile.columns[column]]
        if dfile.index[rows] in bmippl:
            if pd.isna(adding):
                bmiDelArray.append(0)
            else:
                bmiDelArray.append(adding)
        if dfile.index[rows] in ageppl:
            if pd.isna(adding):
                ageDelArray.append(0)
            else:
                ageDelArray.append(adding)
    u, pVal = stats.mannwhitneyu(bmiOrder, bmiDelArray)
    bmiPvals.append(pVal)
    bmiUs.append(u) 

    u, pVal = stats.mannwhitneyu(ageOrder, ageDelArray)
    agePvals.append(pVal)
    ageUs.append(u) 

bmiReject, bmiQvals, e, a = mpt(bmiPvals, 0.05, 'fdr_bh', False, False)

bmiReject, bmiQvals, e, a = mpt(bmiPvals, 0.05, 'fdr_bh', False, False)
