import casanova
from collections import Counter
from matplotlib import pyplot as plt
import pandas 
import numpy as np
from tqdm import tqdm
from itertools import product

MOTCLEFS_BASE = {'Hold_Up', 'Hold-up', 'Holdup', 'Holdup_ledoc', 'HoldUpStopLaPeur'}

def randString(istr):
    l = [(c, c.upper()) if not c.isdigit() else (c,) for c in istr.lower()]
    return ["".join(item) for item in product(*l)]

MOTCLEFS = dict()

for mot in MOTCLEFS_BASE:
    MOTCLEFS[mot] = randString(mot)

GazOnly, tt_Gaz = Counter(), 0
TwintOnly, tt_twint = Counter(), 0
Snsonly, tt_sns = Counter(), 0
ALL, tt_ALL = Counter(), 0
TwintANDSns, tt_TSN = Counter(), 0
TwintANDGazou, tt_TGAZ = Counter(), 0
SnsANDGazou, tt_SGAZ = Counter(), 0

def actualise_counter(row,tweet, Conter, MOTCLEFS):
    for mot in MOTCLEFS:
        for mots in MOTCLEFS[mot]:
            if mots in row[tweet]:
                Conter[mot]+=1

def get_freq(Conter, tt):
    new_c = Counter()
    for x in Conter:
        new_c[x] = Conter[x]/tt
    return new_c

with open('recoltetotale.csv') as f1:
    read = casanova.reader(f1)
    gaz = read.pos.Gazouilloire
    twint = read.pos.Twint
    sns = read.pos.Snscrape
    tweet = read.pos.tweet
    for row in tqdm(read):
        if row[gaz] == '1' and row[twint] == '0' and row[sns] == '0': #Gaz
            actualise_counter(row,tweet,GazOnly,MOTCLEFS)
            tt_Gaz +=1
        elif row[gaz] == '0' and row[twint] == '1' and row[sns] == '0': #Twint
            actualise_counter(row,tweet,TwintOnly,MOTCLEFS)
            tt_twint +=1
        elif row[gaz] == '0' and row[twint] == '0' and row[sns] == '1': #Sns
            actualise_counter(row,tweet,Snsonly,MOTCLEFS)
            tt_sns +=1
        elif row[gaz] == '1' and row[twint] == '1' and row[sns] == '1': #all
            actualise_counter(row,tweet,ALL,MOTCLEFS)
            tt_ALL +=1
        elif row[gaz] == '1' and row[twint] == '0' and row[sns] == '1': #SnsANDGazou
            actualise_counter(row,tweet,SnsANDGazou,MOTCLEFS)
            tt_SGAZ +=1
        elif row[gaz] == '1' and row[twint] == '1' and row[sns] == '0':#GazANDTwint
            actualise_counter(row,tweet,TwintANDGazou,MOTCLEFS)
            tt_TGAZ +=1
        elif row[gaz] == '0' and row[twint] == '1' and row[sns] == '1':#TwintANDSns
            actualise_counter(row,tweet,TwintANDSns,MOTCLEFS)
            tt_TSN +=1

GazOnly2 = get_freq(GazOnly,tt_Gaz)
TwintOnly2 = get_freq(TwintOnly,tt_twint)
Snsonly2 = get_freq(Snsonly, tt_sns)
ALL2 = get_freq(ALL, tt_ALL)
TwintANDSns2 = get_freq(TwintANDSns, tt_TSN)
TwintANDGazou2 = get_freq(TwintANDGazou, tt_TGAZ)
SnsANDGazou2 = get_freq(SnsANDGazou, tt_SGAZ)

l = [(GazOnly,'Gazouilloire'), (TwintOnly,'Twint'), (Snsonly,'Snscrape'), (ALL,'Gaz&Sns&Twint'), (TwintANDSns,'Twint&Sns'), (TwintANDGazou,'Twint&Gazou'), (SnsANDGazou, 'Sns&Gazou')]

for y in l:
    fig, ax1 = plt.subplots()
    size = [x for x in y[0].values()]
    explode = [0.1 for x in range(len(y[0].values()))]
    ax1.pie(size,labels = y[0].keys(),explode=tuple(explode),autopct='%1.1f%%', wedgeprops = {'edgecolor' : 'black'})
    plt.title(y[1])
    plt.show()





