from matplotlib_venn import venn3, venn3_circles 
from matplotlib import pyplot as plt
import csv
import argparse

parser = argparse.ArgumentParser(description='merge Gaz,Twint,Sns files into one and display venn3 diagram')
parser.add_argument('Gazoufile',help='Gazouilloire file')
parser.add_argument('Twintfile',help='Twint file')
parser.add_argument('Snsfile',help='Snscrape file')
args = parser.parse_args()

twint = set()
gaz = set()
sns = set()
all_id = dict()

with open(args.Gazoufile) as f1, open(args.Twintfile) as f2, open(args.Snsfile) as f3:
    read_gaz = csv.DictReader(f1)
    read_twint = csv.DictReader(f2)
    read_sns = csv.DictReader(f3)
    for tweet in read_gaz:
        id_t = tweet['id']
        all_id[id_t] = (tweet.get('created_at', None), tweet.get('retweeted_id',None), tweet.get('text',None))
        gaz.add(id_t)
    for tweet in read_twint:
        id_t = tweet['id']
        all_id[id_t] = (tweet.get('created_at', None), tweet.get('retweeted_id',None),tweet.get('tweet',None))
        twint.add(id_t)
    for tweet in read_sns:
        id_t = tweet['id']
        all_id[id_t] = (tweet.get('created_at', None), tweet.get('retweeted_id',None),tweet.get('text',None))
        sns.add(id_t)

All = twint & gaz & sns
twintANDsns = twint & sns - (All)
twintANDgaz = twint & gaz - (All)
snsANDgaz = sns & gaz - (All)
twint_only = twint - (All | twintANDgaz | twintANDsns)
sns_only = sns - (All | snsANDgaz | twintANDsns)
gaz_only = gaz - (All | snsANDgaz | twintANDgaz)

with open('recoltetotale.csv', 'w') as f4:
    fieldn = ['id', 'created_at', 'rt_id','tweet','Gazouilloire', 'Snscrape', 'Twint']
    recolt_tt = csv.DictWriter(f4, fieldnames = fieldn)
    recolt_tt.writeheader()
    for item in All:
        recolt_tt.writerow({'id' : item, 'created_at' : all_id[item][0], 'rt_id' : all_id[item][1], 'tweet': all_id[item][2], 'Gazouilloire' : 1, 'Snscrape': 1, 'Twint' : 1})
    for item in twintANDsns:
        recolt_tt.writerow({'id' : item, 'created_at' : all_id[item][0], 'rt_id' : all_id[item][1],'tweet': all_id[item][2], 'Gazouilloire' : 0, 'Snscrape': 1, 'Twint' : 1})
    for item in twintANDgaz:
        recolt_tt.writerow({'id' : item, 'created_at' : all_id[item][0], 'rt_id' : all_id[item][1], 'tweet': all_id[item][2],'Gazouilloire' : 1, 'Snscrape': 0, 'Twint' : 1})
    for item in snsANDgaz:
        recolt_tt.writerow({'id' : item, 'created_at' : all_id[item][0], 'rt_id' : all_id[item][1], 'tweet': all_id[item][2],'Gazouilloire' : 1, 'Snscrape': 1, 'Twint' : 0})
    for item in twint_only:
        recolt_tt.writerow({'id' : item, 'created_at' : all_id[item][0], 'rt_id' : all_id[item][1], 'tweet': all_id[item][2],'Gazouilloire' : 0, 'Snscrape': 0, 'Twint' : 1})
    for item in sns_only:
        recolt_tt.writerow({'id' : item, 'created_at' : all_id[item][0], 'rt_id' : all_id[item][1], 'tweet': all_id[item][2],'Gazouilloire' : 0, 'Snscrape': 1, 'Twint' : 0})
    for item in gaz_only:
        recolt_tt.writerow({'id' : item, 'created_at' : all_id[item][0], 'rt_id' : all_id[item][1], 'tweet': all_id[item][2],'Gazouilloire' : 1, 'Snscrape': 0, 'Twint' : 0})


# make venn3 diagram
v = venn3(subsets = (1, 1, 0.2, 1, 0.2, 0.2, 0.1), set_labels = ('Gazouilloire', 'Twint', 'Snscrape'), alpha = 0.6)

labels = ['100', '101', '110', '010', '001', '011', '111']
for label in labels:
    v.get_label_by_id(label).set_text(label)

v.get_label_by_id('100').set_text(str(len(gaz_only)))
v.get_label_by_id('101').set_text(str(len(snsANDgaz)))
v.get_label_by_id('110').set_text(str(len(twintANDgaz)))
v.get_label_by_id('010').set_text(str(len(twint_only)))
v.get_label_by_id('001').set_text(str(len(sns_only)))
v.get_label_by_id('011').set_text(str(len(twintANDsns)))
v.get_label_by_id('111').set_text(str(len(All)))

plt.show()
