from matplotlib import pyplot as plt
from timeanalyse import nbtweets_per_days
import numpy as np
import pandas
import argparse

parser = argparse.ArgumentParser(description='Affiche des infos temporelles par rapport à deux récoltes de tweet')
parser.add_argument('filename1')
parser.add_argument('filename2')
args = parser.parse_args()

plt.style.use('fivethirtyeight')

data = nbtweets_per_days(args.filename1,args.filename2)

twint = data[0]
gazou = data[1]
x = twint.keys()
abcisses = [i.day for i in x]

y1 = [twint[k] for k in x]
y2 = [gazou[k] for k in x]

plt.plot(abcisses,y1, label =args.filename1)
plt.plot(abcisses,y2, label =args.filename2)
plt.title('Number of tweets per day')
plt.legend()
plt.xlabel('Dates')
plt.ylabel('Number of tweets')
plt.show()
