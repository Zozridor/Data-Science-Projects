import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
from matplotlib.pyplot import figure

#setting the style
plt.style.use('fivethirtyeight')
figure(num=None, figsize=(10, 5), dpi=80, facecolor='w', edgecolor='k')

#dataset
df = pd.read_csv("/home/fluffy/Documents/Data Science Files/Financial Crises Final Paper/declining_longterm_yields.csv")

#preparing x axis
dates = []
for value in df.loc[:,'DATE']:
    dates.append(value)
xi = [i for i in range(0, len(dates))]

#iterating through columns and putting values in lists
yields = []
for value in df.loc[:,'bond_yields']:
    yields.append(value)

#defining the axes
ax = plt.axes()
plt.ylim(0,5)
plt.xlim(0,63)
plt.xlabel('Month-Year')
plt.ylabel('10-year Treasury Bond Yields (%)')
plt.title('Declining Yields on Long-Term Assets (US)')

#ax.set_xticklabels(dates)
ax.set_xticks(xi)

#plotting values on the graph
plt.plot(dates, yields, '-r')

#correcting x axis ticks
x = plt.gca().xaxis
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
for item in x.get_ticklabels():
    item.set_rotation(45)

plt.show()