# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma  # 动画函数
n = 100
# zeros(n,定义的类型)，不定义的话默认为浮点数
data = np.zeros(n, dtype=[('postion', float, 2),  # dtype=[位置,类型,维度]#x,y所以是2维度
                          ('size', float, 1),  # 大小,类型，维度
                          ('growth', float, 1),  # 增长，类型，1维度
                          ('color', float, 4)])  # 颜色，类型，红。绿。蓝。透明=4


data['postion'] = np.random.uniform(0, 1, (n, 2))
# 平均该型uniform(satr,end,(行,2列))#二维np.random.uniform(0, 1, (n, 2))
data['size'] = np.random.uniform(50, 750, n)  # 平均该型uniform字体大小(最小,最大,n)#一维
data['growth'] = np.random.uniform(30, 150, n)  # 平均该型uniform增量大小(最小,最大,n)#一维
#  平均该型uniform颜色区间(satr,end,(行,2列))#4列
data['color'] = np.random.uniform(0, 1, (n, 4))
mp.figure('Bubble', facecolor='lightgray')
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
plot = mp.scatter(data['postion'][:, 0], data['postion'][:, 1],
                  s=data['size'], c=data['color'])  # numpy是行优先
# data中'postion'标签中[行，列]


def update(num):
    data['size'] += data['growth']  # 大小+增量达到变大效果
    index = num % n  # num是从1开始的数字，n是终止数字-1
    data['postion'][index] = np.random.uniform(0, 1, 2)  # 一个点 所以不需要二维数组
    data['size'][index] = 0
    data['growth'][index] = np.random.uniform(30, 150)
    data['color'][index] = np.random.uniform(0, 1, 4)
    plot.set_offsets(data['postion'])
    plot.set_sizes(data['size'])  # 提交给图形界面
    plot.set_facecolors(data['color'])
# 1.在位置点达到100时破裂index点的气泡，并随机生成一个新的达到一个循环效果
# 2.从0开始增长所以设置为0
# 3.重新设置增长率(气泡破了之后的增长量)
# 4.将破掉气泡的位置点(index)重新随机生成颜色
# 5.将重新设定的效果提交给图形界面显示


# 声明一个变量确保生命周期,不声明变量的话这个句话只是全局变量，不会执行
mian = ma.FuncAnimation(mp.gcf(), update, interval=10)
# ma.FuncAnimation(mp.gcf()获取当前图, update(更新绘制函数),interval(时间间隔))
mp.show()

# 动画设定流程
# 导入数据，视图,动画模块(import matplotlib.animation)
# 先定义值和值的属性（类型（index,大小,颜色，增长等），数据类型，维度）
# 开始切分这些标签和标签中的行和列
# 声明变量绑定动画函数(获取当前图像,处理绘制函数,自增长的时间间隔)
# 定义绘制函数的具体流程加以处理
# 提交给当前视图，实现动画效果
