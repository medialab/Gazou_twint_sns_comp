import casanova
from collections import Counter
from datetime import datetime, timedelta


def generate_day_series(begin_date,number):
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
    ListCount = {'8/11' : [Counter(),Counter()],
                 '9/11' : [Counter(),Counter()],
                 '10/11' : [Counter(),Counter()],
                 '11/11' : [Counter(),Counter()],
                 '12/11' : [Counter(),Counter()],
                 '13/11' : [Counter(),Counter()],
                 '14/11' : [Counter(),Counter()],
                 '15/11' : [Counter(),Counter()],
                 '16/11' : [Counter(),Counter()]
    }
    with open(file1) as f1, open(file2) as f2:
        twintreader = casanova.reader(f1)
        gazoureader = casanova.reader(f2)
        created_atT = twintreader.pos.created_at
        created_atG = gazoureader.pos.created_at
        for date in twintreader.cells('created_at'):
            date = datetime.fromisoformat(date)
            row_day = date.day
            row_month = date.month
            row_hour = date.hour
            key = ListCount.get(str(row_day)+'/'+str(row_month))
            if key:
                key[0][row_hour] += 1
        for date in gazoureader.cells('created_at'):
            date = datetime.fromisoformat(date)
            row_day = date.day
            row_month = date.month
            row_hour = date.hour
            key = ListCount.get(str(row_day)+'/'+str(row_month))
            if key:
                key[1][row_hour] += 1
    return ListCount