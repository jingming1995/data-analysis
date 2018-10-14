# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
mp.figure('class_one', facecolor='lightgray')  # 必须先figure才能创建子视图


mp.subplot(331)  # subplot(行,列,图形号)
x = np.linspace(-np.pi, np.pi, 1000)
y1 = np.cos(x)
# mp.figure('class_one', facecolor='lightgray')
mp.title('class_one')
mp.xticks(())
mp.yticks(())
mp.plot(x, y1)
# text(上位置，下位置，文本，ha（水平对齐）=参数，va=参数(垂直对齐))
# mp.text(0.5, 0.5, '1', ha='center', va='center', size=30)


mp.subplot(332)
x = np.linspace(-np.pi, np.pi, 1000)
y2 = np.sin(x)
# mp.figure('class_one', facecolor='lightgray')
mp.title('class_one')
mp.xticks(())
mp.yticks(())
mp.plot(x, y2, color='red')
# # text(上位置，下位置，文本，ha（水平对齐）=参数，va=参数(垂直对齐))
# mp.text(0.5, 0.5, '2', ha='center', va='center', size=30)


mp.subplot(333)
x = np.linspace(-np.pi, np.pi, 1000)
y = 2 ** x
# mp.figure('class_one', facecolor='lightgray')
mp.title('class_one')
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2,
           np.pi * 3 / 4, np.pi],
          [r'$-\pi$', r'-$\frac{\pi}{2}$', r'$0$', r'$\frac{pi}{2}$',
           r'$\frac{3\pi}{4}$', r'$\pi$'])

mp.yticks((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

mp.plot(x, y, linestyle='-')
mp.grid(linestyle=':')
# # text(上位置，下位置，文本，ha（水平对齐）=参数，va=参数(垂直对齐))
# mp.text(0.5, 0.5, '3', ha='center', va='center', size=30)


mp.subplot(334)
x = np.linspace(-np.pi, np.pi, 1000)
y = x // 2
# mp.figure('class_one', facecolor='lightgray')
mp.title('class_one')
mp.xticks(())
mp.yticks(())
mp.plot(x, y, linestyle='--', color='orange')
mp.grid(linestyle='-')
# # text(上位置，下位置，文本，ha（水平对齐）=参数，va=参数(垂直对齐))
# mp.text(0.5, 0.5, '4', ha='center', va='center', size=30)


mp.subplot(335)
x = np.linspace(-np.pi, np.pi, 1000)
y1 = np.cos(x)
y2 = np.sin(x)
y3 = x * y1

# mp.figure('class_one', facecolor='lightgray')
mp.title('class_one')
mp.xticks(())
mp.yticks(())
mp.plot(x, y1, linestyle='-', color='blue')
mp.plot(x, y2, linestyle='-', color='red')
mp.plot(x, y3, linestyle='-', color='green')


mp.subplot(336)
n = 10000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
# mp.figure('test_normal', facecolor='lightgray')
d = np.sqrt(x**2 + y**2)
mp.xlabel('x', fontsize=8)
mp.ylabel('y', fontsize=8)
mp.scatter(x, y, s=10, c=d, cmap='jet_r')
mp.title('random_normal')
mp.grid()


mp.subplot(337)
n = 1000
x = np.linspace(0, 8 * np.pi, n)
y1 = np.cos(x) / 2
y2 = np.sin(x)
mp.xlabel('x', fontsize=10)
mp.ylabel('y', fontsize=10)
mp.title('Fill_between')
mp.plot(x, y1, linestyle='-')
mp.plot(x, y2, linestyle='-')
mp.fill_between(x, y1, y2, y1 < y2, color='pink', alpha=0.5)
mp.fill_between(x, y1, y2, y1 > y2, color='green', alpha=0.5)
# mp.fill_betwee('填充区水平坐标',下垂直坐标（star)，上垂直坐标(end),条件表达式,color=颜色,alpho=透明度)

mp.tight_layout()  # 紧凑布局
mp.grid(linestyle=':')
mp.show()
