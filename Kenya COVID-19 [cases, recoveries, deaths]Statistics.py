# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:38:16 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
import seaborn as sns
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
Cases_ = 'https://bit.ly/3e8cPnf'
Recovered = 'https://bit.ly/39YqrxU'
Deaths = 'https://bit.ly/3eboDVB'
sns.set()
df = pd.concat(map(pd.read_csv,[Cases_, Recovered, Deaths]))
df.columns
df = df[df['Country/Region'].str.contains('Kenya')]
df.drop(['Lat', 'Long', 'Province/State'], inplace=True, axis=1)
df=df.reset_index(drop=True)
df=df.set_index('Country/Region').T
df.reset_index(inplace=True)
df=df.loc[df.sum(axis=1)!=0]

df.columns = ['Dates','Confirmed Cases','Recoveries', 'Deaths']
df.reset_index(inplace=True)


fig, ax = plt.subplots(figsize=(15,7))
ax.spines['left'].set_color('#aea6a6')
ax.spines['bottom'].set_color('#aea6a6')

mpl.rcParams['axes.prop_cycle'] = (cycler(color=['#4daf4a', '#377eb8', 
            '#e41a1c']))


p=['Confirmed Cases','Recoveries','Deaths']
df=df.melt(id_vars='Dates', value_vars=p, var_name='',
           value_name='No')

df['Dates'] = pd.to_datetime(df['Dates'], 
  format='%m/%d/%y', errors='raise')

ax=sns.set_style('darkgrid')
ax=sns.lineplot(x='Dates', y='No', hue='',
               data=df, marker='.')

ax.set(title='COVID-19 in Kenya')

ax.annotate('Source:Johns Hopkins School of Public Health           Code:https://github.com/kriskirimi/Covid2019EA',
            fontsize=8, style='italic',xy=(0, 0),xycoords=('axes fraction'), textcoords=('offset points'), 
            xytext=((00, -52)))

bbox=dict(boxstyle='round', fc='none', ec='grey')

ax.annotate('Start of curfew', xycoords='data',xy=('3/27/20',0), 
            xytext=('3/27/20',110), bbox=bbox,
            arrowprops=dict(arrowstyle='-',color='#515050',linestyle='dashed'), fontsize=8,ha='center' )

ax.annotate('Ban on\nInternational Flights', xycoords='data',xy=('3/25/20',0), 
            xytext=('3/25/20',75), bbox=bbox,
            arrowprops=dict(arrowstyle='-',color='#515050', linestyle='dashed'), fontsize=8,ha='center' )

ax.set_xticklabels(labels=df['Dates'],rotation=90, fontsize=8)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_xlim(df['Dates'].min(), df['Dates'].max())
plt.savefig(r'C:\Users\KIRIMI\Documents\GitHub\Covid2019EA\Kenya COVID-19 [cases, recoveries, deaths]Statistics.jpeg',
            format='jpeg', dpi=400)
plt.show()
plt.close()
