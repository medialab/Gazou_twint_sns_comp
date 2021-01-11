from matplotlib import pyplot as plt
from analyse import number_tweetsperhours_by_day
import numpy as np
import pandas

data = number_tweetsperhours_by_day('recolte_sns2.csv','gazou_sansthread.csv')
width = 0.25
days = data.keys()

fig,(ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)
fig2,( ax3, ax4) = plt.subplots(nrows = 2, ncols = 1)
fig3,(ax5, ax6) = plt.subplots(nrows = 2, ncols = 1)
fig4,(ax7, ax8) = plt.subplots(nrows = 2, ncols = 1)
c= 1
for x in days:
    datax = data[x]
    twint = datax[0]
    print(twint)
    gazou = datax[1]
    print(gazou)
    z = twint.keys()
    y1 = [twint[k] for k in z]
    y2 = [gazou[k] for k in z]
    print(z)
    print(y1)
    print(y2)
    df = pandas.DataFrame(dict(n = y1,
                                   m = y2))
    ind = np.arange(len(df))
    if c ==1:
        ax1.barh(ind, df.n, width, label='snscrape')
        ax1.barh(ind + width, df.m, width, label = 'Gazou')
        ax1.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax1.legend()
        ax1.set_title('08-11')
    elif c ==2:
        ax2.barh(ind, df.n, width, label='snscrape')
        ax2.barh(ind + width, df.m, width, label = 'Gazou')
        ax2.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax2.legend()
        ax2.set_title('09-11')
    elif c == 3:
        ax3.barh(ind, df.n, width, label='snscrape')
        ax3.barh(ind + width, df.m, width, label = 'Gazou')
        ax3.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax3.legend()
        ax3.set_title('10-11')
    elif c == 4 :
        ax4.barh(ind, df.n, width, label='snscrape')
        ax4.barh(ind + width, df.m, width, label = 'Gazou')
        ax4.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax4.legend()
        ax4.set_title('11-11')
    elif c == 5:
        ax5.barh(ind, df.n, width, label='snscrape')
        ax5.barh(ind + width, df.m, width, label = 'Gazou')
        ax5.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax5.legend()
        ax5.set_title('12-11')
    elif c == 6:
        ax6.barh(ind, df.n, width, label='snscrape')
        ax6.barh(ind + width, df.m, width, label = 'Gazou')
        ax6.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax6.legend()
        ax6.set_title('13-11')
    elif c == 7:
        ax7.barh(ind, df.n, width, label='snscrape')
        ax7.barh(ind + width, df.m, width, label = 'Gazou')
        ax7.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax7.legend()
        ax7.set_title('14-11')
    elif c == 8:
        ax8.barh(ind, df.n, width, label='snscrape')
        ax8.barh(ind + width, df.m, width, label = 'Gazou')
        ax8.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax8.legend()
        ax8.set_title('15-11')
    c +=1
plt.show()

"""
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
ax.barh(ind, df.n, width, label='twint')
ax.barh(ind + width, df.m, width, label = 'Gazou')

ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
ax.legend()

plt.show()
"""


