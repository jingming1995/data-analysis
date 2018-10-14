# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma  # 动画函数
mp.figure('生成器生成信号波', facecolor='lightgray')
mp.title('Signal')
mp.xlabel('time', fontsize=14)
mp.ylabel('signal', fontsize=14)


ax = mp.gca()
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
plot = mp.plot([], [], c='orangered')[0]
# 还不知道数据是什么所以我们将x,y轴设置为空，为绘制函数提供位置
# 生成是是一个对象的容器所以需要切片取出
plot.set_data([], [])


def updata(data):  # 绘制函数
    t, v = data
    x, y = plot.get_data()  # 取出数据函数
    x.append(t)
    y.append(v)

    x_min, x_max = ax.get_xlim()  # 获取当前图形x轴大小,如果t增长度大于x轴，那么x轴图形大小x2
    print(ax.get_xlim())  # 是一个间距开始和结束，所以需要两个值去接收
    if t > x_max:
        ax.set_xlim(x_min, x_max * 2)
    plot.set_data(x, y)  # 将x,y列表的对象重新写入给plot


def get():  # 用生成器采集数据
    t = 0
    for x in range(10000):
        v = np.sin(2 * np.pi * t) * np.exp(-t / 8)
        yield t, v  # 将t,v抛出并在这个变量供updat调用，并在get函数保存本次循环的执行结果
        t += 0.05

mian = ma.FuncAnimation(mp.gcf(), updata, get, interval=5)
mp.show()
