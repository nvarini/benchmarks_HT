import numpy
import matplotlib.pyplot as plt
import argparse
import colorsys
from collections import defaultdict
from aux_routines import *
import sys

parser = argparse.ArgumentParser()
parser.add_argument("data_file",type=file,nargs='+',help="data_file")
args = parser.parse_args()

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                "%8.0f" % height,
                ha='center', va='bottom')



def count_elements(array,counts):
  for i in array:
    if i not in counts:
      counts.append(i)

times1 = []
times2 = []
speedup1 = []
speedup2 = []
nodes = []

count = 0

f = open('data_file','r')
for line in f:
  words=line.split()
  nodes.append(round(float(words[0]),1))
  times1.append(float(words[2]))
  times2.append(float(words[3][:-1]))
  speedup1.append(times1[0]/float(words[2]))
  speedup2.append(times2[0]/float(words[3][:-1]))


N = len(nodes)
width = 0.35
ind = np.arange(N)

fig, ax = plt.subplots()
rects1 = ax.bar(ind, times1, width, color='g')
rects2 = ax.bar(ind+width, times2, width, color='b')
# add some text for labels, title and axes ticks
ax.set_ylabel('Time to solution(seconds)')
ax.set_xlabel('Number of atoms')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(nodes)
#plt.xticks(x, labels, rotation='vertical')

ax.legend((rects1[0], rects2[0]), ('pw-6.1@fidis', 'pw+sirius@PizDaint'), loc=2)

autolabel(rects1)
autolabel(rects2)
plt.savefig('tts.png')

fig1, ax = plt.subplots()
rects1 = ax.bar(ind, speedup1, width, color='g')
rects2 = ax.bar(ind+width, speedup2, width, color='b')
# add some text for labels, title and axes ticks
ax.set_ylabel('Speedup')
ax.set_xlabel('Number of nodes')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(nodes)
ax.set_title('BaTiO3')

ax.legend((rects1[0], rects2[0]), ('pw-6.1@fidis', 'pw+sirius@PizDaint'), loc=2)

autolabel(rects1)
autolabel(rects2)


plt.savefig('speedup.png')

