import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import figure

plt.style.use('fivethirtyeight')

ax1 =

'''countries = ("China","Indonesia","India","Argentina","South Africa","Turkey",'Mexico')
USD_debt = [5.9, 38.0, 19.7, 47.1, 33.5, 34.1,32.6]
y_pos = np.arange(len(countries))

plt.bar(y_pos, USD_debt, align ='center', alpha=0.5)


ax = plt.axes()
plt.xlim(-1,7)
plt.ylim(-1,100)
plt.ylabel('USD Debt as % of GDP')
plt.title('Dollar-Denominated Debt in EMs')
plt.xticks(np.arange(7), countries)

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

plt.show()'''

turkey = [-6.7,-4.7,-3.7,-3.8,-5.6,-5.2,-4.2]
argentina = [-2.1,-1.6,-2.8,-2.7,-4.8,-5.0,-4.4]
south_africa = [-5.8,-5.1,-4.6,-2.8,-2.4,-3.5,-3.8]
indonesia = [-3.2,-3.1,-2.0,-1.8,-1.7,-2.4,-2.5]

years_x = [2013,2014,2015,2016,2017,2018,2019]

ax = plt.axes()
plt.ylabel('Current Account % of GDP')
plt.title('Current Accounts in EMs')
ax.set_xticks(years_x)

#correcting x axis ticks overlap
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

#plotting values on the graph
plt.ylim(-8,6)
plt.plot(years_x, turkey, 'o--')
plt.plot(years_x,argentina,'o--')
plt.plot(years_x,south_africa,'o--')
plt.plot(years_x,indonesia,'o--')
plt.legend(['Turkey','Argentina','South Africa','Indonesia'])
plt.show()
