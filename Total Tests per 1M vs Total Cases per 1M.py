# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:40:19 2020

@author: KIRIMI
"""

import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
import numpy as np
r = requests.get(r'http://www.worldometers.info/coronavirus/')
df0 = pd.read_html(r.text)
for df in df0:
    print(df)

countries_Af=['Algeria', 'Angola', 
              'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 
              'Cameroon', 'Cabo Verde', 'Cameroon','CAR', 
              'Chad','Congo','Djibouti','DRC','Egypt','Equatorial Guinea',
              'Eritrea', 'Eswatini','Ethiopia','Gabon','Gambia','Ghana', 
              'Guinea','Guinea-Bissau', 'Ivory Coast','Kenya','Lesotho',
              'Liberia','Libya','Madagascar','Malawi','Mali','Mauritania',
              'Mauritius', 'Morocco','Mozambique','Namibia','Niger', 
              'Nigeria','Rwanda','Sao Tome and Principe','Senegal', 
              'Seychelles','Sierra Leone','Somalia','South Africa','South Sudan',
              'Sudan','Tanzania','Togo','Tunisia','Uganda',
              'Western Sahara','Zambia', 'Zimbabwe']


df = df[df['Country,Other'].str.contains(r'^({})$'.format('|'.join(countries_Af)))]

# for i in set(countries_Af):
#     if i in set(df1['Country,Other'].tolist()):
#         pass
#     else:
#         print(i + ' is missing')

df = df.rename(columns={ 'Tot\xa0Cases/1M pop':'Total Cases/1M pop'})

df1 = df[['Country,Other', 'TotalTests','TotalCases', 'Tests/ 1M pop','Total Cases/1M pop' ]]

df1.dropna(axis=0, inplace=True)

fig, ax = plt.subplots(figsize=(13,6))

ax = sns.regplot(data=df1, x='Tests/ 1M pop', 
                y='Total Cases/1M pop',scatter_kws={"s": 70}, robust=True)  

ax.set(xscale='log', yscale='log', title='Correlation Between Tests per 1M Pop and Confirmed Cases Per 1M Pop for Selected African Countries')
    
for line in range(0, df1.shape[0]):
    ax.annotate(df1['Country,Other'].iloc[line], xy=(df1['Tests/ 1M pop'].iloc[line], df1['Total Cases/1M pop'].iloc[line]), 
                xytext=(df1['Tests/ 1M pop'].iloc[line]*1.06,df1['Total Cases/1M pop'].iloc[line]),
            horizontalalignment='left', size='8', color='#4f4c4c')

ax.annotate('Source:https://www.worldometers.info/coronavirus/', (0,0), (00,-35), fontsize=8, 
             xycoords='axes fraction', textcoords='offset points')
ax.annotate('Code:https://github.com/kriskirimi/Covid2019EA', (0,0), (00,-44), fontsize=8, 
             xycoords='axes fraction', textcoords='offset points')

plt.savefig(r'C:\Users\KIRIMI\.spyder-py3\My Projects\Covid 19\Total Tests Per 1M Vs Total Cases Per 1M.jpeg',
            format='jpeg', dpi=400)