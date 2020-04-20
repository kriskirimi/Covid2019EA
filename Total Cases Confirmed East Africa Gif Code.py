# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:02:49 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ImageMagickWriter
df = pd.read_csv('https://bit.ly/3e8cPnf')

East_Africa = (['Kenya', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi', 'Ethiopia', 
                'South Sudan', 'Somalia'])
df = df[df['Country/Region'].str.contains(format('|'.join(East_Africa)))]
df.reset_index(inplace=True, drop=True)

df.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)

df.set_index('Country/Region', inplace=True, drop=True)
df = df.T
df=df.loc[(df.sum(axis=1)!=0)]
df.reset_index(inplace=True)
fig, ax = plt.subplots(figsize=(12,7))
x = df['index']
y1= df['Ethiopia']
y2= df['Kenya']
y3= df['Tanzania']
y4= df['Uganda']
y5= df['Burundi']
y6= df['South Sudan']
y7= df['Somalia']
y8= df['Rwanda']

line1, = ax.plot(x, y1, color='#377eb8')
line2, = ax.plot(x, y2, color='#e41a1c')
line3, = ax.plot(x, y3, color='#4daf4a')
line4, = ax.plot(x, y4, color='#984ea3')
line5, = ax.plot(x, y5, color='#ff7f00')
line6, = ax.plot(x, y6, color='#666666')
line7, = ax.plot(x, y7, color='#a65628')
line8, = ax.plot(x, y8, color='#0c2c84')

                 
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('#525252')
ax.spines['bottom'].set_color('#525252')
         
ax.set_xticklabels(labels= df['index'].iloc[:], rotation=90, fontsize=8)
ax.legend(labels=['Ethiopia', 'Kenya', 'Tanzania', 'Uganda', 'Burundi', 'South Sudan',
       'Somalia', 'Rwanda'], loc='upper left')
ax.set(title='East Africa COVID-19 Confirmed Cases')
plt.style.use('ggplot')

ax.annotate('Source:Johns Hopkins School of Public Health\nCode:https://github.com/kriskirimi/Covid2019EA',
            fontsize=7.5, color='#6b6a6a',style='italic',xy=(0, 0),xycoords=('axes fraction'), textcoords=('offset points'), 
            xytext=((00, -52)))
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
ani.save(r'C:\Users\KIRIMI\Documents\GitHub\Covid2019EA\EA Covid19 Confirmed Cases.gif', writer='imagemagick')
plt.show()
# plt.claose()