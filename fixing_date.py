#fixing date
#recolte une heure en avance sur Gazou
import datetime
import casanova
import csv

def Rconvert_datetime(date):
    d = date[:-4]
    new_date = datetime.datetime(int(d[:4]),int(d[5:7]),int(d[8:10]),int(d[11:13]),int(d[14:16]),int(d[17:]))
    return new_date

with open('recolte_sns.csv') as f1, open('recolte_sns2.csv','w') as f2:
    enricher = casanova.enricher(f1,f2)
    date = enricher.pos.created_at
    for row in enricher:
        row[date] = row[date][:-6]
        enricher.writerow(row)

'''
with open("collecte2_GAZOU.csv") as f1, open("clean_collecte2_gazou.csv",'w') as f2:
    file_content1_reader = csv.reader(f1)
    file2_writer = csv.writer(f2)
    while True:
        try:
            row = file_content1_reader.__next__()
            file2_writer.writerow(row)
        except csv.Error:
            print("Error")
        except StopIteration:
            print("Iteration End")
            break'''