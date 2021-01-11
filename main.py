from matplotlib import pyplot as plt
from analyse import nbtweets_per_days, nbtweets_per_hour
import numpy as np
import pandas 
#print(plt.style.available)

plt.style.use('fivethirtyeight')
"""
data = nbtweets_per_days('recolte_sns2.csv','gazou_sansthread.csv')# it works

twint = data[0]
gazou = data[1]

x = twint.keys()
abcisses = [i.day for i in x]
print(x)
y1 = [twint[k] for k in x]
y2 = [gazou[k] for k in x]

plt.plot(abcisses,y1, label ='snscrape')
plt.plot(abcisses,y2, label ='Gazou')
plt.title('Number of tweets per day')
plt.legend()
plt.xlabel('Dates')
plt.ylabel('Number of tweets')
plt.show()
"""

data = nbtweets_per_hour('recolte_sns2.csv','gazou_sansthread.csv')
twint = data[0]
gazou = data[1]
print(twint)
print('\n')
print(gazou)
x = twint.keys()
y1 = [twint[k] for k in x]
y2 = [gazou[k] for k in x]

df = pandas.DataFrame(dict(graph = ['23', '22','21', '20', '19', '18', '17' , 
                                   '16', '15', '14', '13', '12', '11', 
                                   '10', '9', '8', '7','6', '5', 
                                   '4', '3', '2', '1', '0'],
                                   n = y1,
                                   m = y2))
#
#ab = [i for i in x]
#abx = np.arange(len(ab))
ind = np.arange(len(df))

width = 0.25

fig, ax = plt.subplots()
ax.barh(ind, df.n, width, label='snscrape')
ax.barh(ind + width, df.m, width, label = 'Gazou')

ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
ax.legend()

plt.show()

"""
plt.barh(abx - width,y1, height = width)
plt.barh(abx + width,y2, height = width)
ax.set_yticks( width / 2)
ax.set_yticklabels(('0', '1','2', '3', '4', '5', '6' , '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'))
plt.legend()
plt.show()



df = pandas.DataFrame(dict(graph=['Item one', 'Item two', 'Item three'],
                           n=[3, 5, 2], m=[6, 1, 3])) 


width = 0.4


ax.barh(ind, df.n, width, color='red', label='N')
ax.barh(ind + width, df.m, width, color='green', label='M')

ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
ax.legend()
"""
