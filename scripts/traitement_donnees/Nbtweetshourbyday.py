from matplotlib import pyplot as plt
from timeanalyse import number_tweetsperhours_by_day
import numpy as np
import pandas
import argparse

parser = argparse.ArgumentParser(description='Affiche des infos temporelles par rapport à deux récoltes de tweet')
parser.add_argument('filename1')
parser.add_argument('filename2')
args = parser.parse_args()

data = number_tweetsperhours_by_day(args.filename1,args.filename2)
width = 0.25
days = data.keys()

for x in days:
    datax = data[x]
    twint = datax[0]
    gazou = datax[1]
    z = twint.keys()
    y1 = [twint[k] for k in z]
    y2 = [gazou[k] for k in z]
    df = pandas.DataFrame(dict(n = y1,
                                   m = y2))
    ind = np.arange(len(df))
    fig, ax1 = plt.subplots(nrows = 1, ncols = 1)
    ax1.barh(ind, df.n, width, label='twint')
    ax1.barh(ind + width, df.m, width, label = 'Gazouilloire')
    ax1.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
    ax1.legend()
    ax1.set_title(str(x))

plt.show()