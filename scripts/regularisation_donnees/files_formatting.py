import casanova
from datetime import datetime, timedelta
import argparse

parser = argparse.ArgumentParser(description = 'Normalise data')
parser.add_argument('Gazfile')
parser.add_argument('Twintfile')
parser.add_argument('Snsfile')
parser.add_argument('date1', action = 'store_true', help ='must be isoformat YYYY-MM-DDTHH:MM:SS')
parser.add_argument('date2', action = 'store_true', help ='must be isoformat YYYY-MM-DDTHH:MM:SS')
args = parser.parse_args()

#dealing with Gazfile
with open(args.Gazfile) as f1, open('filtered_gazouilloire.csv','w') as f2:
    enri = casanova.enricher(f1,f2)
    threadon = enri.pos.collected_via_thread_only
    rt = enri.pos.retweeted_id
    date = enri.pos.created_at
    date1 = datetime.fromisoformat(args.date1)
    date2 = datetime.fromisoformat(args.date2)
    for row in enri:
        if row[threadon] == '1':
           continue
        #if row[rt]:
            #continue
        date_r = datetime.fromisoformat(row[date])
        if date_r >= date1 and date_r <= date2:
            enri.writerow(row)


#dealing with SnscrapeFile

#fixing time
with open(args.Snsfile) as f1, open('filtered_sns.csv','w') as f2:
    enricher = casanova.enricher(f1,f2)
    date = enricher.pos.created_at
    for row in enricher:
        row[date] = row[date][:-6]
        enricher.writerow(row)


# dealing with Twintfile

#fixing time

def Rconvert_datetime(date):
    d = date[:-4]
    new_date = datetime.datetime(int(d[:4]),int(d[5:7]),int(d[8:10]),int(d[11:13]),int(d[14:16]),int(d[17:]))
    return new_date

with open(args.Twintfile) as f1, open('filtered_twint.csv','w') as f2:
    enricher = casanova.enricher(f1,f2)
    for row in enricher:
        #row[2] -> created_at
        newcrt = Rconvert_datetime(row[2]) - datetime.timedelta(hours=1)
        row[2] = newcrt.isoformat()
        #row[3] -> date
        row[3] = newcrt.date()
        #row[4] -> time
        row[4] = newcrt.time()

