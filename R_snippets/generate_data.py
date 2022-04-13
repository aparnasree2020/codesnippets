# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:08:13 2022

@author: MC
"""

import os 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import scipy.stats
sns.set(color_codes = True)

in_filepath = "D:/Aparna/dataset/"
out_filepath = "D:/Aparna/dataset/figure/"

out_cat_path = out_filepath + "cat_figs/"
os.makedirs(out_cat_path, exist_ok = True)

out_num_path = out_filepath + "num_figs/"
os.makedirs(out_num_path, exist_ok = True)

data = pd.read_csv(in_filepath+ 'train.csv' )  
data.describe()

cols = data.columns
num_cols = data._get_numeric_data().columns 
cat_cols = list(set(cols) - set(num_cols))

#fig, ax = plt.subplots(figsize = (16,10))

if 0:
    for n, col in enumerate(cat_cols):
        fig = plt.figure()
        data[col].value_counts().plot(kind='bar')
        plt.ylabel("Count")
        plt.xlabel(col)
        plt.title(col)
        plt.tight_layout(pad=1, w_pad=1, h_pad = 1.0)
        fig.savefig(out_cat_path+col+'plot.png', dpi = 300)

if 0: 
    for n, col in enumerate(num_cols):
        fig = plt.figure()
        hist = data[col].hist()
        plt.ylabel("Count")
        plt.xlabel(col)
        plt.title(col)
        plt.tight_layout(pad=1, w_pad=1, h_pad = 1.0)
        fig.savefig(out_num_path+col+'plot.png', dpi = 300)

#getmax, min, median 
for n, col in enumerate(num_cols):
    fig = plt.figure()
    likelihoods, bin_edges, patches = data[col].hist()


# Store existing data's. Histogram. 
    
    
Nsamples = 10000
    
hist = np.histogram(data['Age'].dropna(), bins=100)
hist_dist = scipy.stats.rv_histogram(hist)    

X = np.linspace(min(data['Age']), max(data['Age']), 100)
#plt.hist(data['Age'].dropna(), density=True, bins=100)
#plt.plot(X, hist_dist.pdf(X), label='PDF')
plt.plot(X, hist_dist.cdf(X), label='CDF')
plt.show() 
    
counts, bins = np.histogram(data['Age'].dropna())   
    
Bin_value = data['Age'].value_counts(dropna=False)    
Bins= Bin_value.index

temp = (Nsamples*Bin_value)/len(data['Age'])
newlist = []
for idx, val in enumerate(temp):
    print(Bins[0], int(val)) 
    newlist += [Bins[idx]]*int(val)

newlist += [idx]*int(Nsamples-len(newlist)) # last bin gets left over samples

new_data = pd.DataFrame(columns = num_cols)
new_data['Age'] = newlist

fig = plt.figure()
hist = new_data['Age'].hist()
plt.ylabel("Count")
plt.xlabel(col)
plt.title(col)
plt.tight_layout(pad=1, w_pad=1, h_pad = 1.0)
    
fig = plt.figure()
hist = data['Age'].hist()
plt.ylabel("Count")
plt.xlabel(col)
plt.title(col)
plt.tight_layout(pad=1, w_pad=1, h_pad = 1.0)



    
    
    
    
    
    
    
    
    
#     