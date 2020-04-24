# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:29:51 2020

@author: KIRIMI
"""

import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import folium

url = 'http://www.worldometers.info/coronavirus/'
r = requests.get(url)

df0=pd.read_html(r.text)

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

df1=df[df['Country,Other'].str.contains(r'^({})$'.format('|'.join(countries_Af)), case=False)]
                                        
df1=df1.drop(['NewCases','NewDeaths'], axis=1)
df2=df1.dropna(subset=['Tests/ 1M pop'])
df2.sort_values('Tests/ 1M pop', ascending=False, inplace=True)
df2.reset_index(inplace=True, drop=True)

fig, ax = plt.subplots(figsize=(14, 6))
x = np.arange(len(df2['Country,Other'].unique()))
rect1=ax.barh(x,df2['Tests/ 1M pop'])
ax.set_yticks(np.arange(len(df2['Country,Other'].unique())))
ax.set_yticklabels(df2['Country,Other'])
     
def autolabels(rects):
    for rect in rects:
        xvalue=rect.get_x() + rect.get_width() +.95
        yvalue=rect.get_y() + rect.get_height() - .80
        ax.text(xvalue,yvalue,rect.get_width(), fontsize=8)
        
autolabels(rect1)

EA = (df2['Country,Other']=='Kenya')
for i, b in enumerate(EA):
    if b:
        ax.patches[i].set_facecolor('red')

ax.set(xlabel='Tests/ 1M pop', title='Selected African Countries Coronavirus Tests/1M Population(As of 23rd April 2020)')
ax.annotate('Source:https://www.worldometers.info/coronavirus/', (0,0), (00,-35), fontsize=8, 
             xycoords='axes fraction', textcoords='offset points')
ax.annotate('Code:https://github.com/kriskirimi/Covid2019EA', (0,0), (00,-44), fontsize=8, 
             xycoords='axes fraction', textcoords='offset points')

plt.style.use('seaborn')

gdf=gpd.read_file('C:/Users/KIRIMI/Desktop/New folder/countries_Af.geojson')

geoD = 'C:/Users/KIRIMI/Desktop/New folder/countries_Af.geojson'


# for c in set(countries_Af):
#     if c in set(gdf['name'].tolist()):
#         pass
#     else:
#         print(c + ' is missing')


df1 = df1.rename(columns={'Country,Other':'name'})

merged = gdf.merge(df1, how='left', on = 'name')

m = folium.Map(location=[11.5024338, 17.7578122], 
               zoom_start=4, tiles='CartoDB positron')

df3=merged.dropna(subset=['Tests/ 1M pop'])

df3.drop(['created_at','updated_at'], axis=1, inplace=True)

folium.Choropleth(geo_data = geoD, 
                data=df3, columns=['name','Tests/ 1M pop'],
                key_on='feature.properties.name',
                fill_color= 'RdYlBu',
                fill_opacity=0.8,
                line_opacity=0.3,
                nan_fill_color = '#676767',
                legend_name='Tests').add_to(m)


folium.LayerControl().add_to(m)

m.save(r'C:\Users\KIRIMI\Documents\GitHub\Covid2019EA\Selected African Countries Coronavirus Tests per 1M Population.html')

plt.show()

plt.savefig(r'C:\Users\KIRIMI\Documents\GitHub\Covid2019EA\Selected African Countries Coronavirus Tests per 1M Population.jpeg',
            format='jpeg', dpi=300)

plt.close()

