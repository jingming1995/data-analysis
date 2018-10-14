# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp
import numpy as np
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))  # 构造点阵函数
z = (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)  # exp自然对数e方负x方负y的平方的方
# print(z.shape)#1000,1000
mp.figure('hot ', facecolor='lightgray')
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)


mp.imshow(z, cmap='jet', origin='low')  # 从下到上
mp.colorbar().set_label('z', fontsize=8)
# mp.imshow 热图呈现。只传入函数坐标即可坐标按照矩阵形式。用origin设置坐标轴方向
# mp.colorbar().set_label(函数坐标轴（二维数组）,字体大小)设置颜色区分效果图。会呈现出一个颜色区间条
mp.grid()
mp.tick_params(labelsize=10)
mp.title('hot')
mp.show()
