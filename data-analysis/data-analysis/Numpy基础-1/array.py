# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(10)
print(a)

b = np.arange(1, 10)
print(b)

c = np.arange(1, 10, 2)
print(c)

d = np.array([])
print(d)

e = np.array([10, 20, 30, 50])  # 一维数组
print(e)

f = np.array([
    [1, 2, 3],
    [4, 5, 6]])
print(f)  # 二位数组
print(type(f))
print(type(f[0][0]))  # 这是python的类型
print(f.dtype)  # numpy 自己的类型

g = np.array(['1', '2', '3'], dtype=np.int32)
print(type(g[0]))
print(g.dtype)
print('s', g)

h = g.astype(np.str_)  # 转换成字符串
print('h', h)
print(type(h[0]))
print(type(h.dtype))
print(e.shape)  # 一维数组的4个元素
print(f.shape)  # 两行三列的二维数组
