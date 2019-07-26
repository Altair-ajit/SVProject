import pandas as pd
from pandas import DataFrame as df
from scipy import stats
import bmiList
import numpy as np
from mne.stats import fdr_correction as fdr
import seaborn as sns
sns.set(font_scale = .375)

#initiating the file to be read
deletions = "../data/dsgv.df"
dfile = pd.read_pickle(deletions)
print(dfile.head())

#mann whitney for the columns
ageppl = bmiList.getAgeppl()
bmippl = bmiList.getBMIppl()

taxa = []
sciname = []
binslist = []
for col in dfile.columns:
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

        #re-arrange data into 2 columns to compare deletion and no-deletion
        bmi0 = []
        bmi1 = []
        for dels in range(len(bmiDelArray)):
            if bmiDelArray[dels] == 0:
                bmi0.append(bmiOrder[dels])
            else:
                bmi1.append(bmiOrder[dels])

        age0 = []
        age1 = []
        for dels in range(len(ageDelArray)):
            if ageDelArray[dels] == 0:
                age0.append(ageOrder[dels])
            else:
                age1.append(ageOrder[dels])
                
    u, pVal = stats.mannwhitneyu(bmi0, bmi1)
    bmiPvals.append(pVal)
    bmiUs.append(u) 

    u, pVal = stats.mannwhitneyu(age0, age1)
    agePvals.append(pVal)
    ageUs.append(u) 


bmiReject, bmiQvals = fdr(bmiPvals, 0.05, 'indep')

ageReject, ageQvals = fdr(agePvals, 0.05, 'indep')


#heatmap condtitions
passAge = []
passBMI = []
passTax = []
for count in range(len(agePvals)):
    if agePvals[count] < .1 or bmiPvals[count] < .1:
        passTax.append(taxonomy[count])
        if ageUs[count] < 0:
            passAge.append((agePvals[count] * -1))    
        else:
            passAge.append(agePvals[count])
        if bmiUs[count] < 0:
            passBMI.append((bmiPvals[count] * -1))    
        else:
            passBMI.append(bmiPvals[count])


heatset = np.column_stack((passBMI, passAge))
colors = ["#c7dcff","#99bfff", "#6ba1ff","#0f69fa" ,"#fa2f0f" ,"#ff4f30", "#ff7057", "#fcb3a7"]
reds = ["#fa2f0f" ,"#ff4f30", "#ff7057", "#fcb3a7"]
fig = sns.heatmap(heatset, vmax = .15, vmin = 0, cmap = reds, center = .075, xticklabels = ["BMI", "Age"], yticklabels = passTax)
fig.set(ylabel = "Deletion SVs")
colorbar = fig.collections[0].colorbar
colorbar.set_ticks([.01, .05, .1, 0.15])
colorbar.set_ticklabels(["p<0.01", "p<0.05", "p<0.1","n.s"])
e = fig.get_figure() 
e.savefig("../results/Deletion_SV/MannUWhitneyPvalsHeatmap.png")


passAge = []
passBMI = []
passTax = []
for count in range(len(ageQvals)):
    if ageQvals[count] < .1 or bmiQvals[count] < .1:
        passTax.append(taxonomy[count])
        if ageUs[count] < 0:
            passAge.append((ageQvals[count] * -1))    
        else:
            passAge.append(ageQvals[count])
        if bmiUs[count] < 0:
            passBMI.append((bmiQvals[count] * -1))    
        else:
            passBMI.append(bmiQvals[count])


heatset = np.column_stack((passBMI, passAge))
fig = sns.heatmap(heatset, vmax = .12, vmin = -0.12, cmap = colors, center = 0, xticklabels = ["BMI", "Age"], yticklabels = passTax)
fig.set(ylabel = "Deletion SVs")
colorbar = fig.collections[0].colorbar
colorbar.set_ticks([-0.105, -0.075, -.045,-.015, 0,.015, .045, .075, 0.105])
colorbar.set_ticklabels(["n.s","q<0.1", "q<0.05", "q<0.01", " ", "q<0.01", "q<0.05", "q<0.1","n.s"])
e = fig.get_figure() 
e.savefig("../results/Deletion_SV/MannUWhitneyQvalsHeatmap.png")