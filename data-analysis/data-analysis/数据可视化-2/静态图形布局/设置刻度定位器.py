# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
mp.figure('Locator')
locators = [
    'mp.NullLocator()',
    'mp.MaxNLocator(nbins=3, steps=[1, 3, 5, 7, 9])',
    'mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])',  # 规划刻度显示范围
    'mp.AutoLocator()',  # 自动选择一个最合适的刻度形式
    'mp.IndexLocator(offset=0.5, base=1.5)',  # 从0.5开始每次增加1.5刻度
    'mp.MultipleLocator(2)',  # 缺省值显示刻度，默认为1
    'mp.LinearLocator(numticks=21)',  # 指定21个刻度数
    'mp.LogLocator(base=2, subs=[1.0])']  # 次方LogLocato
n_locators = len(locators)
for i, locator in enumerate(locators):
    mp.subplot(n_locators, 1, i + 1)
    mp.xlim(0, 10)
    mp.ylim(-1, 1)
    mp.yticks(())
    ax = mp.gca()
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.xaxis.set_major_locator(eval(locator))  # 设置主刻度定位器
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))  # 设置主刻度定位器
    mp.plot(np.arange(11), np.zeros(11))  # zeros产生一个全0的数组一共有11位
    mp.text(5, 0.3, locator[3:], ha='center', size=10)
mp.tight_layout()
mp.show()

# 13.刻度定位器
# ax = mp.gca()
# ax.xaxis...
# ax.yaxis...
# set_major_locator(): 设置主刻度定位器
# set_minor_locator(): 设置次刻度定位器
# NullLocator() - 空，不做刻度标记
# MaxNLocator() - 指定最多刻度数
# FixedLocator() - 由参数指定刻度
# AutoLocator() - 默认，自动选择最合理的刻度
# IndexLocator() - 根据偏移和增量定位刻度
# MultipleLocator() - 根据指定的距离定位刻度
# LinearLocator() - 根据指定的刻度数定位刻度
# LogLocator() - 根据指定的底数和指数定位刻度
