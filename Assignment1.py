#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:50:30 2020

@author: tejasvinavnage
"""
### ADDED BY ABHI
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn
import seaborn as sns
import numpy as np

data1 = pd.read_excel("ApplianceShipment.xlsx")

data2 = pd.read_excel("RidingMowers2.xls")


g = sns.scatterplot(x="Income", y="LotSize", hue="Ownership",
              data=data2, palette=['green', 'red'], legend='full')


colormap = np.array(['r', 'g'])

# Question 2
x = data2['Income']
y = data2['LotSize']
categories = data2['Ownership']
plt.scatter(x, y, c = colormap[categories])
plt.show()

data2.plot.scatter('Income', 'LotSize', colormap='jet')


# Question 3
data1.plot(kind='line',x='Quarter',y='Shipments')
plt.show()

data1.sort_values(by=['Quarter'], inplace=True)

#Comment #1
