# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
n = 12
x = np.arange(n)
y1 = (1 - x / n) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x / n) * np.random.uniform(0.5, 1.0, n)


mp.figure('柱状图', facecolor='lightgray')
mp.title('normal_SanDian', fontsize=20),
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
mp.xticks(x + x + 1)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.bar(x, y1, ec='white', fc='orangered', label='bar')
mp.legend()

mp.show()


# c设定边缘色和填充色的，但是赋值了d 那么c就等于颜色+距离，再使用cmap填充颜色区间
# cmap='jet_r'#颜色映射区间 从蓝到红
