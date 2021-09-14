# -*- coding: utf-8 -*-
"""Copy of olympics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cr3XgF9JnYx_7AUW1uXehjoKdNtbiln-

### **Summer Olympics Data Analysis Assignment**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("summer.csv")

print(df)

"""## **1. In how many cities Summer Olympics is held so far?**"""

#df['City'].unique()

data=df['City'].unique()
d=pd.DataFrame(data,columns=['City'])
print('The cities where summer olympics held:')
print(d)
print('Total cities:')
d.count()

"""## **2. Which sport is having most number of Gold Medals so far? (Top 5)**"""

d=df[df['Medal']=='Gold']
print('The Top 5 sport having most number of Gold Medals')
d.groupby('Sport').count()['Medal'].head().sort_values(ascending = False).plot.bar()

"""## **3. Which sport is having most number of medals so far? (Top 5)**

"""

print('The Top 5 sport having most number of  Medals')

df.groupby('Sport').count()['Medal'].head().sort_values(ascending = False).plot.bar()

"""## **4. Which player has won most number of Medals**"""

print('The  player who has won the most number of Medals')
data=df.groupby('Athlete').count()['Medal'].sort_values(ascending = False)
d=pd.DataFrame(data,columns=['Athlete','Medal']).head(1)
print(d)

"""## **5. Which player has won most number Gold Medals of medals? (Top 5)**

"""

d=df[df['Medal']=='Gold']
d.groupby('Athlete').count()['Medal'].sort_values(ascending = False).head().plot.bar()

"""##**6. In which year India won first Gold Medal in Summer Olympics?**"""

d=df[df['Medal']=='Gold']
ds=d[d['Country']=='IND']
print('Data of the year in which India won first Gold Medal in Summer Olympics:')
ds.head(1)

#d.groupby('Y').count()['Year'].sort_values(ascending = False)

"""## **7. Which event is most popular in terms on number of players? (Top 5)**

"""

ev=df.groupby('Event').count()['Athlete'].sort_values(ascending = False).head().plot.bar()

"""## **8. Which sport is having most female Gold Medalists? (Top 5)**

"""

d=df[df['Gender']=='Women']
print('The sport having most female Gold Medalists:')
d.groupby('Sport').count()['Gender'].sort_values(ascending = False).head().plot.bar()