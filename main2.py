from matplotlib import pyplot as plt
from analyse import number_tweetsperhours_by_day
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

fig,(ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)
fig2,( ax3, ax4) = plt.subplots(nrows = 2, ncols = 1)
fig3,(ax5, ax6) = plt.subplots(nrows = 2, ncols = 1)
fig4,(ax7, ax8) = plt.subplots(nrows = 2, ncols = 1)
c= 1
for x in days:
    datax = data[x]
    twint = datax[0]
    print(twint)
    gazou = datax[1]
    print(gazou)
    z = twint.keys()
    y1 = [twint[k] for k in z]
    y2 = [gazou[k] for k in z]
    print(z)
    print(y1)
    print(y2)
    df = pandas.DataFrame(dict(n = y1,
                                   m = y2))
    ind = np.arange(len(df))
    if c ==1:
        ax1.barh(ind, df.n, width, label=args.filename1)
        ax1.barh(ind + width, df.m, width, label =args.filename2)
        ax1.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax1.legend()
        ax1.set_title('08-11')
    elif c ==2:
        ax2.barh(ind, df.n, width, label=args.filename1)
        ax2.barh(ind + width, df.m, width, label = args.filename2)
        ax2.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax2.legend()
        ax2.set_title('09-11')
    elif c == 3:
        ax3.barh(ind, df.n, width, label=args.filename1)
        ax3.barh(ind + width, df.m, width, label =args.filename2)
        ax3.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax3.legend()
        ax3.set_title('10-11')
    elif c == 4 :
        ax4.barh(ind, df.n, width, label=args.filename1)
        ax4.barh(ind + width, df.m, width, label = args.filename2)
        ax4.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax4.legend()
        ax4.set_title('11-11')
    elif c == 5:
        ax5.barh(ind, df.n, width, label=args.filename1)
        ax5.barh(ind + width, df.m, width, label =args.filename2)
        ax5.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax5.legend()
        ax5.set_title('12-11')
    elif c == 6:
        ax6.barh(ind, df.n, width, label=args.filename1)
        ax6.barh(ind + width, df.m, width, label = args.filename2)
        ax6.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax6.legend()
        ax6.set_title('13-11')
    elif c == 7:
        ax7.barh(ind, df.n, width, label=args.filename1)
        ax7.barh(ind + width, df.m, width, label = args.filename2)
        ax7.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax7.legend()
        ax7.set_title('14-11')
    elif c == 8:
        ax8.barh(ind, df.n, width, label=args.filename1)
        ax8.barh(ind + width, df.m, width, label = args.filename2)
        ax8.set(yticks=ind + width, yticklabels=z, ylim=[2*width - 1, len(df)])
        ax8.legend()
        ax8.set_title('15-11')
    c +=1
plt.show()



