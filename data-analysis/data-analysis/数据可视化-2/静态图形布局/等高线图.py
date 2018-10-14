# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp
import numpy as np
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))  # 构造点阵函数
z = (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)  # exp自然对数e方负x方负y的平方的方
# print(z.shape)#1000,1000
mp.figure('等高线图 ', facecolor='lightgray')
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
mp.contourf(x, y, z, cmap='jet')
c = mp.contour(x, y, z, 8, colors='black', linewidths=0.5)
# contourf(水平坐标，垂直坐标，函数（表达式）坐标，线条间距（数量），cmap=(颜色映射))
# colors线条颜色，linewidths线条宽度


mp.clabel(c, inline_spacing=1, fmt='%.1f', fontsize=8)
# inline_spacing 文字和图形的线内空白，防止标签数据压在线上
# fmt=文字格式（%.1f)浮点数保留一位小数


mp.grid()
mp.tick_params(labelsize=10)
mp.title('contourf')
mp.show()
