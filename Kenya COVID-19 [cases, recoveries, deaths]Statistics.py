# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:38:16 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
Cases_ = 'https://bit.ly/3e8cPnf'
Recovered = 'https://bit.ly/39YqrxU'
Deaths = 'https://bit.ly/3eboDVB'

df = pd.concat(map(pd.read_csv,[Cases_, Recovered, Deaths]))

df = df[df['Country/Region'].str.contains('Kenya')]

df.drop(['Lat', 'Long', 'Province/State'], inplace=True, axis=1)

df=df.reset_index(drop=True)

df=df.set_index('Country/Region').T

df.reset_index(inplace=True)

df=df.loc[df.sum(axis=1)!=0]


df.columns = ['Dates','Confirmed Cases','Recoveries', 'Deaths']

df.reset_index(inplace=True)


fig, ax = plt.subplots(figsize=(14,7))
mpl.rcParams['axes.prop_cycle'] = (cycler(color=['#4daf4a', '#377eb8', '#e41a1c']))
mpl.rcParams['font.size'] = 9

p=[df['Confirmed Cases'],df['Recoveries'],df['Deaths']]

for i in p[:len(p)]:
    ax.plot(df['Dates'], i, marker='.')
    
ax.set(title='COVID-19 in Kenya')

ax.annotate('Source:Johns Hopkins School of Public Health\nCode:https://github.com/kriskirimi/Covid2019EA',
            fontsize=7, style='italic',xy=(0, 0),xycoords=('axes fraction'), textcoords=('offset points'), 
            xytext=((00, -49)))

bbox=dict(boxstyle='round', fc='none', ec='grey')

ax.annotate('Start of curfew', xycoords='data',xy=('3/27/20',0), 
            xytext=('3/27/20',110), bbox=bbox,
            arrowprops=dict(arrowstyle='-',color='#6f6f6f',linestyle='dashed'), fontsize=8,ha='center' )

ax.annotate('Ban on\nInternational Flights', xycoords='data',xy=('3/25/20',0), 
            xytext=('3/25/20',75), bbox=bbox,
            arrowprops=dict(arrowstyle='-',color='#6f6f6f', linestyle='dashed'), fontsize=8,ha='center' )
ax.set_xticklabels(labels=df['Dates'],rotation=90, fontsize=8)

ax.legend(labels=['Confirmed Cases','Recoveries','Deaths'],loc='best')

plt.style.use('seaborn-darkgrid')   
plt.savefig(r'C:\Users\KIRIMI\Documents\GitHub\Covid2019EA\Kenya COVID-19 [cases, recoveries, deaths]Statistics.jpeg',
            format='jpeg', dpi=400)
plt.show()

plt.close()
