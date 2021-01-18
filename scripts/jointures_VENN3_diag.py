from matplotlib_venn import venn3, venn3_circles 
from matplotlib import pyplot as plt
import casanova

twint = set()
gaz_id = set()
sns = set()
snsIGazou = set()
snsITwint= set()
TwintIGazou= set()
AllI = set()

with open('gazou_sansthread.csv') as f1, open('clean_twint_fr.csv') as f2, open('recolte_sns_fixeddate.csv') as f3:
    read_gaz = casanova.reader(f1)
    read_twint = casanova.reader(f2)
    read_sns = casanova.reader(f3)
    for id_g in read_gaz.cells('id'):
        gaz_id.add(id_g)
    for id_T in read_twint.cells('id'):
        if id_T in gaz_id:
            TwintIGazou.add(id_T)
            twint.add(id_T)
        else:
            twint.add(id_T)
    for id_Sns in read_sns.cells('id'):
        if id_Sns in gaz_id and id_Sns in twint:
            AllI.add(id_Sns)
            snsIGazou.add(id_Sns)
            snsITwint.add(id_Sns)
            sns.add(id_Sns)
        elif id_Sns in gaz_id:
            snsIGazou.add(id_Sns)
            sns.add(id_Sns)
        elif id_Sns in twint:
            snsITwint.add(id_Sns)
            sns.add(id_Sns)
        else:
            sns.add(id_Sns)
         #cells

#deal with all those sets to fit them just right and get len
gaz_id2 = gaz_id - TwintIGazou - snsIGazou
twint2 = twint - TwintIGazou - snsITwint
sns2 = sns - snsIGazou - snsITwint
snsITwint2 = snsITwint - AllI
snsIGazou2 = snsIGazou - AllI
TwintIGazou2 = TwintIGazou - AllI
'''
with open('clean_twint_fr.csv') as f1, open('twint_onlyof3.csv', 'w') as f2:
    enr = casanova.enricher(f1,f2)
    for row, idt in enr.cells('id', with_rows = True):
        if idt in twint2:
            enr.writerow(row)
with open('recolte_sns2.csv') as f1, open('sns_onlyof3.csv', 'w') as f2:
    enr = casanova.enricher(f1,f2)
    for row, idt in enr.cells('id', with_rows = True):
        if idt in sns2:
            enr.writerow(row)
with open('clean_twint_fr.csv') as f1, open('snsItwint.csv', 'w') as f2:
    enr = casanova.enricher(f1,f2)
    for row, idt in enr.cells('id', with_rows = True):
        if idt in snsITwint2:
            enr.writerow(row)

'''
### make jointures first

#subsets = (1, 1, 0.2, 1, 0.2, 0.2, 0.1) size of venn diagrams

#labels = ['100', '101', '110', '010', '001', '011', '111'] numbers that will be displayed
v = venn3(subsets = (1, 1, 0.2, 1, 0.2, 0.2, 0.1), set_labels = ('Gazouilloire', 'Twint', 'Snscrape'), alpha = 0.6)


labels = ['100', '101', '110', '010', '001', '011', '111']
for label in labels:
    v.get_label_by_id(label).set_text(label)

v.get_label_by_id('100').set_text(str(len(gaz_id2)))
v.get_label_by_id('101').set_text(str(len(snsIGazou2)))
v.get_label_by_id('110').set_text(str(len(TwintIGazou2)))
v.get_label_by_id('010').set_text(str(len(twint2)))
v.get_label_by_id('001').set_text(str(len(sns2)))
v.get_label_by_id('011').set_text(str(len(snsITwint2)))
v.get_label_by_id('111').set_text(str(len(AllI)))

"""
labels2 = [len(gaz_id2), len(twint2), len(TwintIGazou2), len(sns2), len(snsIGazou2), len(snsITwint2), len(AllI)]
for i in range(len(labels)):
    v.get_label_by_id(labels[i]).set_text(str(labels2[i]))
"""
"""
for x in v.subset_labels:
    print(x)"""

plt.show()