import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.font_manager
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd

#objective: show nominal crude steel prodution in China vs the EU and USA in the form of a stack plot

#setting the style
plt.style.use('fivethirtyeight')
figure(num=None, figsize=(7, 5), dpi=100, facecolor='w', edgecolor='k')

#importing the dataset
#units are in mmt (million metric tons)
df = pd.read_csv("/home/fluffy/Documents/Data Science Files/edge_consulting/sti_steel_makingcapacity.csv")

#preparing the x-axis
years = []
for year in df.loc[:,'YEAR']:
    if year in years:
        break
    else:
        years.append(year)

#preparing regional datasets
china = []
eu = []
usa = []
world = []

#appending values to the datasets
china.append(df.loc[lambda df: df['COUNTRY'] == 'CHN','Value'])
eu.append(df.loc[lambda df: df['COUNTRY'] == 'EU28','Value'])
usa.append(df.loc[lambda df: df['COUNTRY'] == 'USA','Value'])
world.append(df.loc[lambda df: df['COUNTRY'] == 'WLD','Value'])

#defining and correcting the axes
ax = plt.axes()
plt.xlabel('Year')
plt.ylabel('Nominal Crude Steel Capacity (mmt)')
plt.xticks(years)
#plt.xticks(range(0, int(plt.xticks()[0][-1])+1, 1))

#correcting x-axis tick rotation
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)
plt.xlim(2000,2017)


#adding legend
ax.plot([],[], color='C0', label='China', linewidth=5)
ax.plot([],[], color='C1', label='EU', linewidth=5)
ax.plot([],[], color='C2',label='USA', linewidth=5)

#creating the stack plot
plt.stackplot(years,china,eu,usa,alpha=0.95)
leg = plt.legend(loc = 'upper left')

plt.show()


