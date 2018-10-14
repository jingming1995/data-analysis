# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d  # 导入3d类型
n = 10000
x = np.random.normal(0, 1, n)  # 现在有1w个点  # x轴随机生成均值为0标准差为1之间的正态分布散点
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)   # 现在有1w个点  #  y轴随机生成均值为0标准差为1之间的正态分布散点
d = np.sqrt(x**2 + y**2)
# 现在有1w个点  # x**2 + y**2平方相加，在用sqrt开方算出散点距离
mp.figure('正态分布散点图', facecolor='white')
ax = mp.gca(projection='3d')  # 用gca 创建三维对象
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
ax.scatter(x, y, z, s=10, c=d, cmap='jet_r', alpha=0.5)
mp.grid()
mp.title('3D Scatter')
mp.show()


# c设定边缘色和填充色的，但是赋值了d 那么c就等于颜色+距离，再使用cmap填充颜色区间
# cmap='jet_r'#颜色映射区间 从蓝到红
