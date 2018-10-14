# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import axes3d  # 导入3d类型
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))  # 构造点阵函数
z = (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)  # exp自然对数e方负x方负y的平方的方
# z = (1 * x + y**3)


ax = mp.gca(projection='3d')  # 用gca 创建三维对象
mp.title('3D Surface')
ax.set_xlabel('x', fontsize=10)  # 在3d图上设定坐标轴标签
ax.set_ylabel('y', fontsize=10)
ax.set_zlabel('z', fontsize=10)
mp.tick_params(labelsize=10)
ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap='jet')
#ax.plot_surface(水平坐标轴, 垂直坐标轴, 函数坐标轴, rstride=行步距, cstride=列步距, cmap=颜色映射)
# rstride=行距, cstride=列步距设定越小，需要做的处理量越大，所需的时间越多，生成的时间越慢
mp.show()
