# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
mp.figure('区域填充')
n = 1000
x = np.linspace(0, 8 * np.pi, n)
y1 = np.cos(x) / 2
y2 = np.sin(x)
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
mp.plot(x, y1, linestyle='-')
mp.plot(x, y2, linestyle='-')
mp.fill_between(x, y1, y2, y1 < y2, color='red', alpha=0.5)
# mp.fill_betwee('填充区水平坐标',下垂直坐标（star)，上垂直坐标(end),条件表达式,color=颜色,alpho=透明度)
mp.fill_between(x, y1, y2, y1 > y2, color='green', alpha=0.5)
mp.title('Fill', fontsize=20)
mp.grid()
mp.show()
