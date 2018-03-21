#coding:gbk

################################################################
####    A 2D Drawing Program
####    About scatter in  logarithmic coordinates
####    Version of October 16, 2016
####    Last update Jan.09, 2017
####    Lu Niu
################################################################

import csv
import matplotlib
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import numpy as np
import os
import pylab
import random
import sys

from matplotlib import cbook
from matplotlib import cm
from matplotlib import pyplot
from matplotlib import rc
from matplotlib.colors import LightSource
from matplotlib.ticker import FormatStrFormatter, LinearLocator, MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plt.subplots()
plt.rc('font', family='serif')
fig.suptitle(r'Suptitle $f^{\prime\prime}(0)$', fontsize=20)    

with open('data of moon.txt', 'r') as fig:
    x = []
    y = []
    for line in fig:
        data = line.split()
        x.append((float(data[0])))
        y.append((float(data[1])))
ColorM = '#F67210'
plt.scatter(x,y, c=ColorM, s=16, alpha=0.8, marker='o', antialiased=True, label=r'Label $f^{\prime\prime}(0)$')
ax.semilogx(x,y, alpha=0)

plt.legend(loc='upper left', fontsize=14, fancybox=True, shadow=False)
plt.xlim(0, 10000)
plt.ylim(0.594, 0.601)
plt.xticks([0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], [r'$10^{-4}$', r'$10^{-3}$', r'$10^{-2}$', r'$10^{-1}$', r'$1$', r'$10$', r'$10^{2}$', r'$10^{3}$', r'$10^{4}$'], fontsize=16)
plt.yticks([0.594, 0.595, 0.596, 0.597, 0.598, 0.599, 0.600, 0.601], [r'$0.594$', r'$0.595$', r'$0.596$', r'$0.597$', r'$0.598$', r'$0.599$', r'$0.600$', r'$0.601$'], fontsize=16)
plt.xlabel(r'$N$', family='serif', fontsize=16)
plt.ylabel(r'$f^{\prime\prime}(0)$', family='serif', fontsize=16)
plt.grid()

plt.savefig('F\'\'(0).eps', dpi=1024)
plt.savefig('F\'\'(0).png', dpi=256)
plt.show()



