import casanova
from collections import Counter
from datetime import datetime, timedelta
from tqdm import tqdm
import math

MOTCLEFS = {'Hold_Up', 'Hold-up', 'Holdup', 'HoldUpStopLaPeur'}

def generate_day_series(begin_date,number):
    begin = datetime.fromisoformat(begin_date)
    while number != 0:
        yield begin
        begin = begin + timedelta(days=1)
        number -= 1

liste_jours = [d for d in generate_day_series('2020-11-08T18:30:00',9)]
#gazou_sth_0816.csv, twint_onlyof3.csv, sns_onlyof3.csv, snsItwint.csv
#tracer histogrammes ? 
def get_freq_word_day(file1,file2,file3,file4,mot,date):
    freq_tw03 = 0
    freq_sns03 = 0
    freq_snsItw3 = 0
    freq_gaz = 0
    tt_tw3, tt_sns3, tt_I, tt_g = 0, 0, 0, 0
    with open(file1) as f1, open(file2) as f2, open(file3) as f3, open(file4) as f4:
        tw3 = casanova.reader(f1)
        twee_tw3 = tw3.pos.tweet
        date_tw3 = tw3.pos.created_at
        sn3 = casanova.reader(f2)
        twee_sn3 = sn3.pos.text
        date_sn3 = sn3.pos.created_at
        Inter = casanova.reader(f3)
        twee_Inter = Inter.pos.tweet
        date_Inter = Inter.pos.created_at
        gz = casanova.reader(f4)
        twee_gz = gz.pos.text
        date_gz = gz.pos.created_at
        for row in tw3:
            mot_t = row[twee_tw3]
            date_t = datetime.fromisoformat(row[date_tw3])
            date_plus_oned = date + timedelta(days=1)
            if date_t > date and date_t < date_plus_oned:
                if mot in mot_t:
                    freq_tw03 += 1
                tt_tw3 +=1
        for row in Inter:
            mot_t = row[twee_Inter]
            date_t = datetime.fromisoformat(row[date_Inter])
            date_plus_oned = date + timedelta(days=1)
            if date_t > date and date_t < date_plus_oned:
                if mot in mot_t:
                    freq_snsItw3 += 1
                tt_I +=1
        for row in sn3:
            mot_t = row[twee_sn3]
            date_t = datetime.fromisoformat(row[date_sn3])
            date_plus_oned = date + timedelta(days=1)
            if date_t > date and date_t < date_plus_oned:
                if mot in mot_t:
                    freq_sns03 += 1
                tt_sns3 +=1
        for row in gz:
            mot_t = row[twee_gz]
            date_t = datetime.fromisoformat(row[date_gz])
            date_plus_oned = date + timedelta(days=1)
            if date_t > date and date_t < date_plus_oned:
                if mot in mot_t:
                    freq_gaz += 1
                tt_g +=1
    result1 = 0
    result2 = 0
    result3 = 0
    n = tt_tw3 + tt_sns3 + tt_I
    try:
        result1 = (freq_sns03 + freq_tw03 + freq_snsItw3)/n
        result2 = freq_gaz/tt_g
        result3 = (freq_sns03 + freq_tw03 + freq_snsItw3 + freq_gaz)/(n + tt_g)
    except:
        pass
    return(result1,result2,result3,n,tt_g)

def get_freq_word_day2(file1,file2,file4,mot,date):
    freq_tw03 = 0
    freq_sns03 = 0
    freq_gaz = 0
    tt_tw3, tt_sns3, tt_g = 0, 0, 0
    with open(file1) as f1, open(file2) as f2, open(file4) as f4:
        tw3 = casanova.reader(f1)
        twee_tw3 = tw3.pos.tweet
        date_tw3 = tw3.pos.created_at
        sn3 = casanova.reader(f2)
        twee_sn3 = sn3.pos.text
        date_sn3 = sn3.pos.created_at
        gz = casanova.reader(f4)
        twee_gz = gz.pos.text
        date_gz = gz.pos.created_at
        for row in tw3:
            mot_t = row[twee_tw3]
            date_t = datetime.fromisoformat(row[date_tw3])
            date_plus_oned = date + timedelta(days=1)
            if date_t > date and date_t < date_plus_oned:
                if mot in mot_t:
                    freq_tw03 += 1
                tt_tw3 +=1
        for row in sn3:
            mot_t = row[twee_sn3]
            date_t = datetime.fromisoformat(row[date_sn3])
            date_plus_oned = date + timedelta(days=1)
            if date_t > date and date_t < date_plus_oned:
                if mot in mot_t:
                    freq_sns03 += 1
                tt_sns3 +=1
        for row in gz:
            mot_t = row[twee_gz]
            date_t = datetime.fromisoformat(row[date_gz])
            date_plus_oned = date + timedelta(days=1)
            if date_t > date and date_t < date_plus_oned:
                if mot in mot_t:
                    freq_gaz += 1
                tt_g +=1
    result1 = 0
    result2 = 0
    result3 = 0
    n = tt_tw3 + tt_sns3 
    try:
        result1 = (freq_sns03 + freq_tw03)/n
        result2 = freq_gaz/tt_g
        result3 = (freq_sns03 + freq_tw03 + freq_gaz)/(n + tt_g)
    except:
        pass
    return(result1,result2,result3,n,tt_g)

liste = []

for mot in MOTCLEFS:
    for day in tqdm(liste_jours):
        liste.append([mot+str(day), get_freq_word_day2('clean_twint_fr.csv', 'recolte_sns_fixeddate.csv','gazou_sth_0816.csv',mot, day)])

RC_s = []


for x in liste:
    rt = 1
    date = x[0]
    p1 = x[1][0]
    p2 = x[1][1]
    p = x[1][2]
    n = x[1][3]
    m = x[1][4]
    #division by 0 
    if p != 0:
        RC = abs(p1-p2)/math.sqrt(p*(1-p)*(1/n + 1/m))
        if RC > 1.96: # seuil de 95 % 
            rt = 0
    RC_s.append([date,rt])

print(RC_s)

'''
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
'''