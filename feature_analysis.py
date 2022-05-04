import pandas as pd
import sys
from pandas import ExcelWriter
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
file='D:/NSN/data1/test_data_final_PASS.xlsx'
parameters_file='D:/NSN/data1/parameters_important_row.xlsx'
newdata=pd.read_excel(parameters_file)
data=pd.read_excel(file)
params=55
no_sfc_pass=126
no_sfc_fail=25
j=0

####Algorithm:01

for l in range(no_sfc_pass):
    newdata=newdata.append({'SFC':data.values[j][3]},ignore_index=True)
    for k in range(params):
        newdata.loc[l][data.values[j][0]]=data.values[j][1]
        j+=1        
newdata=newdata.set_index('SFC')
c=newdata.columns[newdata.dtypes.eq(object)]
newdata[c]=newdata[c].apply(pd.to_numeric,errors='coerce',axis=1)

writer=ExcelWriter('D:/NSN/data1/Data_arranged_pass.xlsx')
newdata.to_excel(writer,'Sheet1')
writer.save()

cor_dat=newdata.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(cor_dat, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(21, 12))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(cor_dat, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
