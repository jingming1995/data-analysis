# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# import numpy as np
# a = np.array([[[1, 2, 3], [2, 3, 3]], [[1, 1, 1], [6, 6, 6]]])  # 三维数组
# print(a[0][1][0])  # 页，行，列

# # 循环遍历
# for x in range(a.shape[0]):  # 页
#     for y in range(a.shape[1]):  # 行
#         for z in range(a.shape[2]):  # 列
#             print(a[x][y][z])  # 或a(x,y,z)
#----------------------------------------------------------------


# import numpy as np
# a = np.array(['1234'])
# print(a.dtype)  # 字符串类型 U4 unicode 小端绪的4个字节
# b = a.dtype = int  # 类型转换int
# print(b)
# c = np.array(['5678'], dtype=int)
# print(c.dtype)  # 可以指定32int 和64int
#--------------------------------------------------------


# import numpy as np
# a = np.array([('1234', ((5, 6), (7, 8)))], dtype={
#              'one': ('U4', 0), 'two': ('(2,2)i4', 16)})  # 二维数组 int类型 4个元素
# print(a, a.dtype)
# # print(len(a))
# # print(a[0]['one'])  # 第0个下标的one键值对

# b = np.array([('1234', ((5, 6), (7, 8)))],
#              dtype={'names': ['one', 'two'], 'formats': ['U4', '(2,2)i4']})
# print(b, b.dtype)

# c = np.array([('1234', ((5, 6), (7, 8)))],
#              dtype=[('one', 'U4'), ('two', '(2,2)i4')])
# print(c, c.dtype)
#-------------------------------------------------------------------------


# import numpy as np
# a = np.array([0x1234], dtype=('u2', {'lo': ('u1', 0), 'li': ('u1', 1)}))
# print(a[0])
# print('{:x} {:x} {:x}'.format(a[0], a['lo'][0], a['li'][0]))
# # 可以当做两种类型去看，u2和键值对
#-------------------------------------------------------------------------


# # 自定义一个numpy复合类型(对象)
# # 字段名，字段类型，字段维度
# test = np.dtype([('name', np.str_, 40), ('age', np.uint8, 1)])
# o = np.array([('Jimmy', 80)], dtype=test)
# print(o[0])
#-------------------------------------------------------------------------


# import numpy as np
# b = np.arange(1, 25).reshape(2, 3, 4)  # 两页三行四列
# print(b)
# print(b[:, 0, 0])  # ：是所有页 页行列
# print(b[0, 1, ::2])  # 第0页 第1行 列从首到尾步长是2
# print(b[0, 1], [1, 3])  # 第0页的第一行，和第二页的第三行，这种方式属于下标集合
# print(b[-1, 1:, 2:])  # 最后一页 第一行第二列后的所有数值
#-------------------------------------------------------------------------

# import numpy as pn
# a = pn.arange(1, 9)  # 8 一维

# b = a.reshape(2, 4)  # 8 二维
# print(b)

# c = b.reshape(2, 2, 2)  # 8 三维
# print(c)

# d = c.ravel()  # 转换成一维
# print(d)

# a += 10  # 原数改变其他处理结果均改变，实现实际数据共享
# print(a, b, c, d, sep='\n')
#--------------------------------------------------------

# import numpy as np
# a = np.arange(11, 20).reshape(3, 3)
# # print(a)
# b = a.flatten()  # 复制变维 将实际数据复制后更改已复制
# a += 10
# print(a)
# print(b)
# x = a.ndim  # 几维度数组
# print(x)
#-----------------------------------------------------------------

import numpy as pn
a, b = pn.arange(1, 10).reshape(3, 3), pn.arange(11, 20).reshape(3, 3)
# print(a, b)
c = pn.hstack((a, b))  # 将两个一维数组合并
# print(c)
l, m = pn.hsplit(c, 2)
print(m, l, sep='\n')

d = pn.column_stack((a, b))  # 列组合
print(d)
