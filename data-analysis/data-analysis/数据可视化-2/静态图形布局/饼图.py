# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp

values = [26, 17, 21, 29, 11]  # 值
spaces = [0.01, 0.01, 0.01, 0.01, 0.01]  # 间隙数组
labels = ['python', 'java', 'c++', 'c#', 'PHP']  # 标签数组
colors = ['blue', 'orange', 'green', 'violet', 'gold']
mp.figure('Pie', facecolor='lightgray')
mp.title('Pie')
mp.pie(values, spaces, labels, colors, '%d%%', shadow=True)  # %d%% %d整数%%百分号
# pie(值数组,间隙数组,标签数组,颜色数组,标签数组，shadow=布尔值（阴影效果),startangle=角度(从多少度开始画饼图)）
mp.axis('equal')  # 等轴属性，不受窗口比例影响保持圆形
mp.show()
