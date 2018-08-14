# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:56:59 2018

@author: CB1118
"""
#%pylab inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

subway_df = pd.read_csv('nyc-subway-weather.csv')

data_by_location = subway_df.groupby(['latitude','longitude'],as_index=False).mean()
print(data_by_location.head()['latitude'])

scaled_entries = (data_by_location['ENTRIESn_hourly'] / 
                  data_by_location['ENTRIESn_hourly'].std())

plt.scatter(data_by_location['latitude'], data_by_location['longitude'],
            s=scaled_entries)