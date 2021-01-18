import casanova
from collections import Counter
from matplotlib import pyplot as plt
import pandas 
import numpy as np

MOTCLEFS = {'Hold_Up', 'Hold-up', 'Holdup', 'Holdup_ledoc', 'HoldUpStopLaPeur'}

#gazou_sth_0816.csv, twint_onlyof3.csv, sns_onlyof3.csv, snsItwint.csv
#tracer histogrammes ? 

freq_tw03 = Counter()
freq_sns03 = Counter()
freq_tw = Counter()
freq_sns = Counter()
freq_snsItw = Counter()
freq_gazItw = Counter()
freq_gazIsns = Counter()
freq_gaz = Counter()
tt_tw3, tt_tw, tt_sns3, tt_sns, tt_I, tt_g = 0, 0, 0, 0, 0,0

with open('twint_onlyof3.csv') as f1, open('sns_onlyof3.csv') as f2, open('snsItwint.csv') as f3, open('GazouIsns.csv') as f4, open('GazouItwint.csv') as f5, open('gazou_sth_0816.csv') as f6:
    tw3 = casanova.reader(f1)
    sn3 = casanova.reader(f2)
    Inter = casanova.reader(f3)
    tw = casanova.reader(f5)
    sn = casanova.reader(f4)
    gz = casanova.reader(f6)
    for text in tw3.cells('tweet'):
        for mot in MOTCLEFS:
            if mot in text:
                freq_tw03[mot] += 1
                tt_tw3 +=1
    for text in sn3.cells('text'):
        for mot in MOTCLEFS:
            if mot in text:
                freq_sns03[mot] += 1
                tt_sns3 +=1
    for text in Inter.cells('tweet'):
        for mot in MOTCLEFS:
            if mot in text:
                freq_snsItw[mot] += 1
                tt_I +=1
    for text in tw.cells('text'):
        for mot in MOTCLEFS:
            if mot in text:
                freq_tw[mot] += 1
                tt_tw +=1
    for text in sn.cells('text'):
        for mot in MOTCLEFS:
            if mot in text:
                freq_sns[mot] += 1
                tt_sns +=1
    for text in gz.cells('text'):
        for mot in MOTCLEFS:
            if mot in text:
                freq_gaz[mot] += 1
                tt_g +=1
for x in freq_tw03:
    freq_tw03[x] /= tt_tw3
for x in freq_sns03:
    freq_sns03[x] /= tt_sns3
for x in freq_snsItw:
    freq_snsItw[x] /= tt_I
for x in freq_sns:
    freq_sns[x] /= tt_sns
for x in freq_tw:
    freq_tw[x] /= tt_tw
for x in freq_gaz:
    freq_gaz[x] /= tt_g

print('twint03')
print(freq_tw03)
print('sns03')
print(freq_sns03)
print('InterSns3Twint3')
print(freq_snsItw)
print('GazIsns')
print(freq_sns)
print('GazItwint')
print(freq_tw)
print("gaz")
print(freq_gaz)
# matplotlib
x = freq_tw03.keys()
x1 = freq_sns03.keys()
x2 = freq_snsItw.keys()
x3 = freq_tw.keys()
x4 = freq_sns.keys()
tw03 = [freq_tw03['Hold_Up'], freq_tw03['Hold-up'],freq_tw03['Holdup'],freq_tw03['HoldUpStopLaPeur']]
sns03 = [freq_sns03['Hold_Up'], freq_sns03['Hold-up'],freq_sns03['Holdup'],freq_sns03['HoldUpStopLaPeur']]
Intsnstw =[freq_snsItw['Hold_Up'], freq_snsItw['Hold-up'],freq_snsItw['Holdup'],freq_snsItw['HoldUpStopLaPeur']]
Intgztw = [freq_tw['Hold_Up'], freq_tw['Hold-up'],freq_tw['Holdup'],freq_tw['HoldUpStopLaPeur']]
gaz = [freq_gaz['Hold_Up'], freq_gaz['Hold-up'],freq_gaz['Holdup'],freq_gaz['HoldUpStopLaPeur']]
#Intgzsns =  [freq_sns[k] for k in x4]
print(tw03)
print(sns03)
print(Intsnstw)
print(Intgztw)
#print(Intgzsns)

df = pandas.DataFrame(dict(graph = ['Hold_Up', 'Hold-up', 'Holdup', 'HoldUpStopLaPeur'],
                            n = tw03,
                            m = sns03,
                            g = Intsnstw,
                            y = Intgztw,
                            z = gaz))
                                   #z = Intgzsns))
ind = np.arange(len(df))

width = 0.10

fig, ax = plt.subplots()
ax.bar(ind, df.n, width, label='Twint_only')
ax.bar(ind + width, df.m, width, label = 'snscrape_only')
ax.bar(ind + 2*width, df.g, width, label = 'Intersection_sns_twint')
ax.bar(ind + 3*width, df.y, width, label = 'Intersection_gazouilloire twint')
ax.bar(ind + 4*width, df.z, width, label = 'Gazouilloire')

ax.set(xticks=ind + width, xticklabels=df.graph)#, ylim=[2*width - 1, len(df)])
ax.legend()

plt.show()
