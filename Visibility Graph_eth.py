# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:03:14 2022

@author: satvi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from visibility_graph import visibility_graph

ds_btc = pd.read_csv('Q:/Non Linear Dynamics/Visibility Graph/Stock Prices/ETH-USD 1-01-2020 -- 31-12-2021.csv')

#btc_close = ds_btc.loc[:, ['Date', 'Close']]
btc_close = ds_btc['Close']

g = visibility_graph(btc_close)
nodes = g.nodes()
edges = g.edges()

def degree_(nodes_, edges_):
    node = nodes_
    dict_ = {}
    #the output here is in the form {node, degree}

    for i in node:
        if i not in dict_:
            dict_[i] = 0

        for j, k in edges:
            if i == j:
                dict_[i] += 1
            if i == k:
                dict_[i] += 1
    return dict_

def degree_distribution(dict_):
    distribution_ = {}
    #this dictionary contains {degree, number of times that degree occured}
    for i in dict_.values():
        if i not in distribution_:
            distribution_[i] = 0
        distribution_[i] += 1
    return distribution_

degree = degree_(nodes, edges)
degree_distribution = degree_distribution(degree)
print(degree_distribution)

xValues = np.log(list(degree_distribution.keys()))
yValues = np.log(list(degree_distribution.values()))
#print(xValues, yValues)

plt.scatter(xValues, yValues, 1.5)
plt.xlabel("k")
plt.ylabel("P(k)")