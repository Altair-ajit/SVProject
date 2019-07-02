import pandas as pd
from pandas import DataFrame as df


deletions = "vsgv.df"
dfile = pd.read_pickle(deletions)

print(dfile.shape)
normalBMI = {}
highBMI = {}

young = {}
median = {}
old = {}

print(dfile.head())
# #lists for people exhibiting specific traits
# bmiNorm = []
# bmiHigh = []


# #iterates through data set obtaining percentages for deletions given phenotyps 
# normdel = 0
# highdel = 0

# for column in range(dfile.shape[1]):
#     for rows in range(dfile.shape[0]):
#         if data.head().index[rows] in bmiNorm:
#             adding = dfile.iloc[rows][dfile.columns[column]]
#             if adding == "NaN":
#                 normdel += 0
#             else:
#                 normdel += adding
#         elif data.head().index[rows] in bmiHigh:
#             adding = dfile.iloc[rows][dfile.columns[column]]
#             if adding == "NaN":
#                 hihgdel += 0
#             else:
#                 highdel += adding


