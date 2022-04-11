# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 01:21:53 2022

@author: satvi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from visibility_graph import visibility_graph

ds_btc = pd.read_csv('Q:/Non Linear Dynamics/Visibility Graph/Stock Prices/BTC-USD 1-01-2020 -- 31-12-2021.csv')

btc_plot_close = ds_btc[['Date', 'Close']]

btc_plot_close.plot()