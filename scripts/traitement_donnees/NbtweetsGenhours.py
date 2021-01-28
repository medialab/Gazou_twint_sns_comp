from matplotlib import pyplot as plt
from timeanalyse import nbtweets_per_hour
import numpy as np
import pandas
import argparse

parser = argparse.ArgumentParser(description='Affiche des infos temporelles par rapport à deux récoltes de tweet')
parser.add_argument('filename1')
parser.add_argument('filename2')
parser.add_argument("--hours", action = 'store_true')
args = parser.parse_args()

plt.style.use('fivethirtyeight')

data = nbtweets_per_hour(args.filename1,args.filename2)
twint = data[0]
gazou = data[1]
x = twint.keys()
y1 = [twint[k] for k in x]
y2 = [gazou[k] for k in x]

df = pandas.DataFrame(dict(graph = ['23', '22','21', '20', '19', '18', '17',
                                    '16', '15', '14', '13', '12', '11',
                                    '10', '9', '8', '7','6', '5',
                                    '4', '3', '2', '1', '0'],
                                    n = y1,
                                    m = y2))

ind = np.arange(len(df))
width = 0.25

fig, ax = plt.subplots()
ax.barh(ind, df.n, width, label=args.filename1)
ax.barh(ind + width, df.m, width, label = args.filename2)

ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
ax.legend()

plt.show()