import pandas as pd
from pandas import DataFrame as df
from scipy import stats
import bmiList
import numpy as np
from mne.stats import fdr_correction as fdr
import seaborn as sns
sns.set(font_scale = .375)

#initiating the file to be read
variables = "../data/vsgv.df"
vfile = pd.read_pickle(variables)
ageppl = bmiList.getAgeppl()
bmippl = bmiList.getBMIppl()

taxa = []
sciname = []
binslist = []
for col in vfile.columns:
    tax, bins = bmiList.parseName(col)
    taxa.append(tax)
    binslist.append(bins)

sciname = bmiList.getTax(taxa)
taxonomy = []
for count in range(len(sciname)):
    fullname = sciname[count] + binslist[count]
    taxonomy.append(fullname)


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
                bmiVarArray.append(0.0)
            else:
                bmiVarArray.append(adding)
        if vfile.index[rows] in ageppl:
            if pd.isna(adding):
                ageVarArray.append(0.0)
            else:
                ageVarArray.append(adding)

    
    bmiSpear = np.column_stack((bmiOrder, bmiVarArray))
    rho, pval = stats.spearmanr(bmiSpear)
    bmiRHO.append(rho)
    bmiPvals.append(pval)
        
    ageSpear = np.column_stack((ageOrder, ageVarArray))
    rho, pval = stats.spearmanr(ageSpear)
    ageRHO.append(rho)
    agePvals.append(pval)
    

bmiReject, bmiQvals = fdr(agePvals, 0.05, 'indep')

ageReject, ageQvals = fdr(agePvals, 0.05, 'indep')

#P VALUE HEATMAP
passAge = []
passBMI = []
passTax = []
for count in range(len(agePvals)):
    if agePvals[count] < .1 or bmiPvals[count] < .1:
        passTax.append(taxonomy[count])
        if ageRHO[count] < 0:
            passAge.append((agePvals[count] * -1)) 
        else:
            passAge.append(agePvals[count])
        if bmiRHO[count] < 0:
            passBMI.append((bmiPvals[count] * -1))    
        else:
            passBMI.append(bmiPvals[count])


heatset = np.column_stack((passBMI, passAge))
colors = ["#c7dcff","#99bfff", "#6ba1ff","#0f69fa" ,"#fa2f0f" ,"#ff4f30", "#ff7057", "#fcb3a7"]
fig = sns.heatmap(heatset, vmax = .12, vmin = -0.12, cmap = colors, center = 0, xticklabels = ["BMI", "Age"], yticklabels = passTax, square = True, label = 'small')
fig.set(ylabel = "Variable SVs")
colorbar = fig.collections[0].colorbar
colorbar.set_ticks([-0.105, -0.075, -.045,-.015, 0,.015, .045, .075, 0.105])
colorbar.set_ticklabels(["n.s","p<0.1", "p<0.05", "p<0.01", " ", "p<0.01", "p<0.05", "p<0.1","n.s"])
e = fig.get_figure() 
e.savefig("../results/Variable_SV/SpearmanPvalsHeatmap.png")

#Q VALUE HEATMAP
passAge = []
passBMI = []
passTax = []
for count in range(len(ageQvals)):
    if ageQvals[count] < .1 or bmiQvals[count] < .1:
        passTax.append(taxonomy[count])
        if ageRHO[count] < 0:
            passAge.append((ageQvals[count] * -1))    
        else:
            passAge.append(ageQvals[count])
        if bmiRHO[count] < 0:
            passBMI.append((bmiQvals[count] * -1))    
        else:
            passBMI.append(bmiQvals[count])


heatset = np.column_stack((passBMI, passAge))
fig = sns.heatmap(heatset, vmax = .12, vmin = -0.12, cmap = colors, center = 0, xticklabels = ["BMI", "Age"], yticklabels = passTax, square = True, label = 'small')
fig.set(ylabel = "Variable SVs")
e = fig.get_figure() 
e.savefig("../results/Variable_SV/SpearmanQvalsHeatmap.png")
