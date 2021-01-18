import casanova
from collections import Counter
from datetime import datetime, timedelta
# dates are great

def generate_day_series(begin_date,number):
    #date_debut should be
    begin = datetime.fromisoformat(begin_date)
    while number != 0:
        yield begin
        begin = begin + timedelta(days=1)
        number -= 1

def nbtweets_per_days(file1,file2):
    with open(file1) as f1, open(file2) as f2:
        readerf1 = casanova.reader(f1)
        readerf2 = casanova.reader(f2)
        liste_jours = [d for d in generate_day_series('2020-11-08T18:30:00',9)]
        print(liste_jours)
        counterfile1 = Counter()
        counterfile2 = Counter()
        created1pos = readerf1.pos.created_at
        created2pos = readerf2.pos.created_at
        for row in readerf1:
            date = datetime.fromisoformat(row[created1pos])
            for i in range(len(liste_jours)-1):
                try:
                    if liste_jours[i] < date < liste_jours[i+1]:
                        counterfile1[liste_jours[i]]+=1
                except:
                    print(date)
                    print(liste_jours[i])
        for row in readerf2:
            date = datetime.fromisoformat(row[created2pos])
            for i in range(len(liste_jours)-1):
                if liste_jours[i] < date < liste_jours[i+1]:
                    counterfile2[liste_jours[i]]+=1
    return(counterfile1, counterfile2)

def nbtweets_per_hour(file1,file2):
    with open(file1) as f1, open(file2) as f2:
        readerf1 = casanova.reader(f1)
        readerf2 = casanova.reader(f2)
        hours = [i for i in range(24)]
        print(hours)
        counterfile1 = Counter()
        counterfile2 = Counter()
        created1pos = readerf1.pos.created_at
        created2pos = readerf2.pos.created_at
        for row in readerf1:
            date = datetime.fromisoformat(row[created1pos])
            hour = date.hour
            for i in range(len(hours)):
                if hours[i] == hour:
                    counterfile1[hours[i]]+=1
        for row in readerf2:
            date = datetime.fromisoformat(row[created2pos])
            hour = date.hour
            for i in range(len(hours)):
                if hours[i] == hour:
                    counterfile2[hours[i]]+=1
    return(counterfile1, counterfile2)

#testing

def number_tweetsperhours_by_day(file1,file2):
    ListCount = {'8' : [Counter(),Counter()],
                 '9' : [Counter(),Counter()],
                 '10' : [Counter(),Counter()],
                 '11' : [Counter(),Counter()],
                 '12' : [Counter(),Counter()],
                 '13' : [Counter(),Counter()],
                 '14' : [Counter(),Counter()],
                 '15' : [Counter(),Counter()],
                 '16' : [Counter(),Counter()]
    }
    with open(file1) as f1, open(file2) as f2:
        twintreader = casanova.reader(f1)
        gazoureader = casanova.reader(f2)
        created_atT = twintreader.pos.created_at
        created_atG = gazoureader.pos.created_at
        for date in twintreader.cells('created_at'):
            date = datetime.fromisoformat(date)
            row_day = date.day
            row_hour = date.hour
            key = ListCount.get(str(row_day))
            if key:
                key[0][row_hour] += 1
        for date in gazoureader.cells('created_at'):
            date = datetime.fromisoformat(date)
            row_day = date.day
            row_hour = date.hour
            key = ListCount.get(str(row_day))
            if key:
                key[1][row_hour] += 1
    return ListCount




if __name__ == '__main__':
    data = number_tweetsperhours_by_day('recolte_sns2.csv','clean_holdup_gazou.csv')
    clef1 = data.keys()
    tt = []
    for x in clef1:
        clef1_1 = data[x][0]
        clef1_2 = data[x][1]
        rt_1, rt_2 = 0,0
        for y in clef1_1:
            rt_1 += clef1_1[y]
        for z in clef1_2:
            rt_2 += clef1_2[z]
        tt.append(rt_1/rt_2)
    print(tt)
    """data2 = number_tweetsperhours_by_day('.csv','gazou_sansthread_sanssearch.csv')
    print(data2)
    clef12 = data2.keys()
    tt2 = []
    for x in clef12:
        clef1_1 = data2[x][0]
        clef1_2 = data2[x][1]
        rt_1, rt_2 = 0,0
        for y in clef1_1:
            rt_1 += clef1_1[y] 
        for z in clef1_2:
            rt_2 += clef1_2[z]
        try:
            tt2.append(rt_1/rt_2)
        except: 
            tt2.append(1)
    #print(tt)
    print(tt2)
    #tt3 = [tt2[x]-tt[x] for x in range(len(tt))]
    #print(tt3)"""

