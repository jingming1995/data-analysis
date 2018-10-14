# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-5, 5, 1000)
y = x**2
y2 = x**2

mp.figure('对数坐标', facecolor='lightgray')

mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)

mp.subplot(211)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))  # 主刻度单位
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))  # 次刻度单位
ax.yaxis.set_major_locator(mp.MultipleLocator(1.0))  # 主刻度单位
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.1))  # 次刻度单位

ax.grid(which='major', axis='both', linewidth=0.5, color='orangered')  # 设置主坐标线
# ax.grid(which=主刻度，axis=取x/y轴/both是x,y轴全设置，color=颜色，线宽等)
ax.grid(which='minor', axis='both', linewidth=0.03, color='red')  # 设置次坐标线
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 使用对数坐标参数和用法和plot完全一致
mp.plot(x, y2, c='blue', label=r'$y=x^2$')
mp.title('plot')
# 使用plot生成图

mp.subplot(212)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))  # 主刻度单位
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))  # 次刻度单位
ax.yaxis.set_major_locator(mp.MultipleLocator(1.0))  # 主刻度单位
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.1))  # 次刻度单位

ax.grid(which='major', axis='both', linewidth=0.5, color='orangered')  # 设置主坐标线
# ax.grid(which=主刻度，axis=取x/y轴/both是x,y轴全设置，color=颜色，线宽等)
ax.grid(which='minor', axis='both', linewidth=0.03, color='red')  # 设置次坐标线
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(x, y, c='orangered', label=r'$y=x^2$')  # exp自然对数有限循环小数（2.7）
mp.legend()
mp.title('semilogy')
# 使用semilogy生成对数图像
mp.show()
