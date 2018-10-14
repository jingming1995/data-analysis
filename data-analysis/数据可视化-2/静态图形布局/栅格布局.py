# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import numpy as np
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
mp.figure('Gridspec')
gs = mg.GridSpec(3, 3)
# 三行三列的布局
mp.subplot(gs[0, :2])  # 根据布局来设置图形大小类似tkinter布局
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '1', ha='center', va='center', size=30, color='yellow')

mp.subplot(gs[1:, 0])  # 根据布局来设置图形大小类似tkinter布局
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '2', ha='center', va='center', size=30, color='green')

mp.subplot(gs[2, 1:])  # 根据布局来设置图形大小类似tkinter布局
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '3', ha='center', va='center', size=30, color='blue')

mp.subplot(gs[:2, 2])  # 占用0行和第3列
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '4', ha='center', va='center', size=30, color='red')

mp.subplot(gs[1, 1])  # 根据布局来设置图形大小类似tkinter布局
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '5', ha='center', va='center', size=30, color='brown')

mp.tight_layout()  # 紧凑布局
mp.show()
