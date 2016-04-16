# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 22:30:32 2016

@author: Bryce Manubay
"""

import pandas as pd
import numpy as np
import pylab as pl


pwd = "C:\\Users\\Bryce Manubay\\Desktop\\UCB\\Shirts Group\\OpenFF\\Ken Kroenlein\\"


b0 = pd.read_csv(pwd+"x1_counts_all.csv", header = -1, index_col = False)
b1 = pd.read_csv(pwd+"x1_counts_dens.csv", header = -1, index_col = False)
b2 = pd.read_csv(pwd+"x1_counts_act.csv", header = -1, index_col = False)
b3 = pd.read_csv(pwd+"x1_counts_emv.csv", header = -1, index_col = False)
b4 = pd.read_csv(pwd+"x1_counts_eme.csv", header = -1, index_col = False)
b5 = pd.read_csv(pwd+"x1_counts_emhp.csv", header = -1, index_col = False)
b6 = pd.read_csv(pwd+"x1_counts_sos.csv", header = -1, index_col = False)
b7 = pd.read_csv(pwd+"x1_counts_dielec.csv", header = -1, index_col = False)

c0 = pd.read_csv(pwd+"x2_counts_all.csv", header = -1, index_col = False)
c1 = pd.read_csv(pwd+"x2_counts_dens.csv", header = -1, index_col = False)
c2 = pd.read_csv(pwd+"x2_counts_act.csv", header = -1, index_col = False)
c3 = pd.read_csv(pwd+"x2_counts_emv.csv", header = -1, index_col = False)
c4 = pd.read_csv(pwd+"x2_counts_eme.csv", header = -1, index_col = False)
c5 = pd.read_csv(pwd+"x2_counts_emhp.csv", header = -1, index_col = False)
c6 = pd.read_csv(pwd+"x2_counts_sos.csv", header = -1, index_col = False)
c7 = pd.read_csv(pwd+"x2_counts_dielec.csv", header = -1, index_col = False)

d0 = pd.read_csv(pwd+"mix_counts_all.csv", header = -1, index_col = False)
d1 = pd.read_csv(pwd+"mix_counts_dens.csv", header = -1, index_col = False)
d2 = pd.read_csv(pwd+"mix_counts_act.csv", header = -1, index_col = False)
d3 = pd.read_csv(pwd+"mix_counts_emv.csv", header = -1, index_col = False)
d4 = pd.read_csv(pwd+"mix_counts_eme.csv", header = -1, index_col = False)
d5 = pd.read_csv(pwd+"mix_counts_emhp.csv", header = -1, index_col = False)
d6 = pd.read_csv(pwd+"mix_counts_sos.csv", header = -1, index_col = False)
d7 = pd.read_csv(pwd+"mix_counts_dielec.csv", header = -1, index_col = False)


pl.figure(1) # All data
#N = 10 
#width = 0.2
#ind = np.arange(N)
#fig, ax = pl.subplots()
#rects1 = ax.bar(ind, np.array([b0[1][0,1,2,3,4],c0[1][0:5]]), width, color='r')
#ax.set_ylabel('Components')
#ax.set_title('Data counts by molecule')
#ax.set_xticks(ind + width)
#ax.set_xticklabels((np.array([b0[1][0:5],c0[1][0:5]])))
#pl.show()
b0[1][0:5].plot(kind = 'bar')



