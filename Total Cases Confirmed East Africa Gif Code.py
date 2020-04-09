# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:02:49 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ImageMagickWriter
df = pd.read_csv(r'C:\Users\KIRIMI\Documents\GitHub\Covid2019EA\Data\time_series_covid19_confirmed_global.csv')
df.dtypes
East_Africa = (['Kenya', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi', 'Ethiopia', 
                'South Sudan', 'Somalia'])
df = df[df['Country/Region'].str.contains(format('|'.join(East_Africa)))]
df.reset_index(inplace=True, drop=True)

df.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)

df.set_index('Country/Region', inplace=True, drop=True)
df = df.T
df=df.loc[(df.sum(axis=1)!=0)]
df.reset_index(inplace=True)
fig, ax = plt.subplots(figsize=(11,7))
x = df['index']
y1= df['Ethiopia']
y2= df['Kenya']
y3= df['Tanzania']
y4= df['Uganda']
y5= df['Burundi']
y6= df['South Sudan']
y7= df['Somalia']
y8= df['Rwanda']
line1, = ax.plot(x, y1, color='#7f65c4')
line2, = ax.plot(x, y2, color='#a6b102')
line3, = ax.plot(x, y3, color='#7241d8')
line4, = ax.plot(x, y4, color='#9dc4e2')
line5, = ax.plot(x, y5, color='#73a6f2')
line6, = ax.plot(x, y6, color='#3526bd')
line7, = ax.plot(x, y7, color='#912b3d')
line8, = ax.plot(x, y8, color='#cb2094')

ax.set_xticklabels(labels= df['index'].iloc[:], rotation=90, fontsize=8)
ax.legend(labels=['Ethiopia', 'Kenya', 'Rwanda', 'Somalia', 'Tanzania', 'Uganda',
       'Burundi', 'South Sudan'], loc='upper left')
ax.set(xlabel='Dates', ylabel='Code:https://github.com/kriskirimi/Covid2019EA\n\nNo of Confirmed Cases', title='East Africa COVID-19 Confirmed Cases')
plt.style.use('seaborn-whitegrid')

def animate(i):
    line1.set_data(x[:i],y1[:i])
    line2.set_data(x[:i],y2[:i])
    line3.set_data(x[:i],y3[:i])
    line4.set_data(x[:i],y4[:i])
    line5.set_data(x[:i],y5[:i])
    line6.set_data(x[:i],y6[:i])
    line7.set_data(x[:i],y7[:i])
    line8.set_data(x[:i],y8[:i])
    return [line1, line2, line3, line4, line5, line6, line7, line8]

ani = FuncAnimation(fig, animate, frames=len(x), interval=400)
writer = ImageMagickWriter(fps = 20)
ani.save(r'C:\Users\KIRIMI\Documents\GitHub\Covid2019EA\Covid19.gif', writer='imagemagick')
plt.show()
