# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:41:49 2019

@author: jmcau
"""

import pandas as pd
from matplotlib.pyplot import pie, axis, show
from pandas import DataFrame
import matplotlib.pyplot as plt

rawdata = pd.read_csv('bills.csv', names = ["Company", "Account Name","Year", "Month", "Day", "Value","Type"])
rawdata[["Year", "Month", "Day"]] = rawdata[["Year", "Month", "Day"]].apply(pd.to_numeric)

#chart1
scatter = DataFrame(rawdata,columns=['Year','Value'])
scatter.plot(x ='Year', y='Value', kind = 'scatter', c='red')

#chart2
rawdata['Type'].value_counts().sort_index().plot.barh()

#chart3
compbreakdown = rawdata.groupby(rawdata["Company"])["Value"].sum()
pie(compbreakdown, labels=compbreakdown.index);
show()

#chart4
rawdata.plot.hexbin(x='Year', y='Value',gridsize=30, figsize=(8,8), title="Year vs Bill Amounts")
plt.show()

