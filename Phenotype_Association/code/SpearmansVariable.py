import pandas as pd
from pandas import DataFrame as df
from scipy import stats
import numpy as np
import statsmodels
import bmiList
from statsmodels.stats.multitest import multipletests as mpt

#initiating the file to be read
variables = "../data/vsgv.df"
vfile = pd.read_pickle(variables)

ageppl = bmiList.getAgeppl()
bmippl = bmiList.getBMIppl()

bmiOrder = []
ageOrder = []

for rows in range(vfile.shape[0]):
    rname = vfile.index[rows]
    if vfile.index[rows] in bmippl:
        bmiOrder.append(bmiList.getBMI(rname))
    if vfile.index[rows] in ageppl:
        ageOrder.append(bmiList.getAge(rname))

#spearman for the columns

bmiRHO = []
bmiPvals = []


ageRHO = []
agePvals = []

for column in range(vfile.shape[1]):
    bmiVarArray = []
    ageVarArray = []
    for rows in range(vfile.shape[0]):
        adding = vfile.iloc[rows][vfile.columns[column]]
        if vfile.index[rows] in bmippl:
            if pd.isna(adding):
                bmiVarArray.append(0)
            else:
                bmiVarArray.append(adding)
        if vfile.index[rows] in ageppl:
            if pd.isna(adding):
                ageVarArray.append(0)
            else:
                ageVarArray.append(adding)
    
    bmiSpear = np.stack((bmiOrder, bmiVarArray))
    rho, pval = stats.spearmanr(bmiSpear)
    bmiRHO.append(rho)
    bmiPvals.append(pval)

    ageSpear = np.column_stack((ageOrder, ageVarArray))
    rho, pval = stats.spearmanr(ageSpear)
    ageRHO.append(rho)
    agePvals.append(pval)

print(bmiPvals)
print(agePvals)

bmiReject, bmiQvals, e, a = mpt(bmiPvals, 0.05, 'fdr_bh', False, False)

ageReject, ageQvals, e, a = mpt(agePvals, 0.05, 'fdr_bh', False, False)

#heatmap condtitions
