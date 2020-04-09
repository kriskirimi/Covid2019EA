# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:24:54 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
df = pd.read_csv(r'C:\Users\KIRIMI\.spyder-py3\My Projects\Covid 19\Data\time_series_covid19_confirmed_global.csv')
df.dtypes
East_Africa = (['Kenya', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi', 'Ethiopia', 
                'South Sudan', 'Somalia'])
df = df[df['Country/Region'].str.contains(format('|'.join(East_Africa)))]
df.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
df.set_index('Country/Region', inplace=True, drop=True)
df = df.T
df=df.loc[(df.sum(axis=1)!=0)]
len(df.columns)
df=df.reset_index()
df=df.rename(columns={'index':'Dates'})
#curfew_Dates=[KE--3/27/20, RW-3/22/20, UG--3/31/20]
curfew_Dates = ['3/27/20', '3/22/20', '3/31/20']
df[df['Dates'].isin(curfew_Dates)]
plt.style.use('bmh')

mpl.rcParams['axes.prop_cycle'] = (cycler(color=['#e41a1c', 
           '#cab2d6', '#708090', '#948d10', '#8856a7', '#fc8d62', 
           '#66c2a5', '#205937']))
           
mpl.rcParams['axes.labelsize'] = 10
mpl.rcParams['axes.titlesize'] = 15
mpl.font_manager.FontProperties(family='fantasy')

fig, ax = plt.subplots(figsize=(11,7))
x = df['Dates']
y1= df['Kenya']
y2= df['Uganda']
y3= df['Rwanda']
y4= df['Tanzania']
y5= df['Somalia']
y6= df['South Sudan']
y7= df['Ethiopia']
y8= df['Burundi']

i=[ df['Kenya'], df['Uganda'], df['Rwanda'],df['Tanzania'], 
   df['Somalia'], df['South Sudan'],df['Ethiopia'], df['Burundi']]

for n in i[:len(i)]:
    ax.plot(df['Dates'],n)

ax.set_xticklabels(labels= df['Dates'].iloc[:], rotation=90, fontsize=8)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('#000000')
ax.spines['bottom'].set_color('#000000')

ax.legend(labels=['Kenya', 'Uganda', 'Rwanda','Tanzania', 'Somalia', 
                  'South Sudan', 'Ethiopia', 
                  'Burundi'], loc='upper left')

ax.set(xlabel='Dates', ylabel='Code:https://github.com/kriskirimi/Covid2019EA\n\nNo of Confirmed Cases', 
       title='East Africa Countries Confirmed COVID-19 Cases')

bbox=dict(boxstyle='round', fc='none', ec='grey')

ax.annotate('Start of curfew\nin Kenya', xycoords='data',xy=('3/27/20',31), 
            xytext=('3/26/20',75), bbox=bbox,
            arrowprops=dict(arrowstyle='->',color='red'), fontsize=8,ha='center' )

ax.annotate('Start of curfew\nin Uganda', xycoords='data',xy=('3/31/20',44), 
            xytext=('4/3/20',60),bbox=bbox,
            arrowprops=dict(arrowstyle='->',color='red'), fontsize=8,ha='center' )

ax.annotate('Start of curfew\nin Rwanda', xycoords='data',xy=('3/22/20',19), 
            xytext=('3/22/20',60),bbox=bbox,
            arrowprops=dict(arrowstyle='->',color='red'), fontsize=8,ha='center' )

ax.annotate('Source:Johns Hopkins School of Public Health',
            fontsize=8,xy=(0, 0),xycoords=('axes fraction'), textcoords=('offset points'), 
            xytext=((00, -48)))
plt.show()
