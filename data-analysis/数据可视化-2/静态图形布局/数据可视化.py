# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as mp  # 绘制图形函数
x = np.linspace(-np.pi, np.pi, 1000)  # 正拍和负pai 生成999个点
y1 = np.cos(x) / 2  # 余弦函数
y2 = np.sin(x)  # 正正弦函数


# 设置特殊点(3pi/4)
xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)
mp.figure('cor/sin', facecolor='white')  # 窗口标题，facecolor 背景颜色
mp.title('Numpy_one', fontsize=20)  # 图形标题


# 垂直坐标轴 设定正负值得方位  min(...)小再左 max(...)大再右
mp.xlim(x.min() * 1.5, x.max() * 1.5)
mp.ylim(min(y1.min(), y2.min()) * 1.5,  # 设置水平坐标轴 设置空白边界
        max(y1.max(), y2.max()) * 1.5)
# 如果边界值是未知的设置坐标轴前可以将余弦和正弦两组数据进行比对求出最大最小值

mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2,
           np.pi * 3 / 4, np.pi],
          [r'$-\pi$', r'-$\frac{\pi}{2}$', r'$0$', r'$\frac{pi}{2}$',
           r'$\frac{3\pi}{4}$', r'$\pi$'])
# 设置水平轴刻度标签
# 第一个是位置参数，第二个是刻度标签，r防止py中是转义，$$说明需要使用键盘中没有的字符
# frac分数{分子}{分母}
mp.yticks((-1, -0.5, 0, 0.5, 1))  # 设置水平坐标轴


ax = mp.gca()  # 设置水平坐标轴函数
ax.spines['left'].set_position(['data', 0])  # 设置轴水平、垂直中心(坐标类型，轴位置)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_color('none')  # 将无用的刻度线颜色取消
ax.spines['right'].set_color('none')
# ax.xaxis.set_ticks_position('top')  # 将x轴刻度数据放在最上方
# ax.yaxis.set_ticks_position('right')  # 将y轴刻度数据放在最右边


mp.plot(x, y1, linestyle='--', linewidth=1.5,
        color='blue', label=r'$y1=\frac{1}{2}cos(x)$')  # label设置图例文本显示


mp.plot(x, y2, linestyle=':', linewidth=3, color='pink',
        label=r'$y2=sin(x)$')  # label设置图例文本显示
# 生成曲线,linestyle设置线型;limewidth设置线型间距;color设置线型颜色


# mp.plot([xo, xo], [yo_cos, yo_sin], linestyle='-',
#         marker='o', linewidth=0.8, color='red')  # marker确定点的形状

mp.plot([xo, xo], [yo_cos, yo_sin], linestyle='none')
mp.scatter([xo, xo], [yo_cos, yo_sin],
           color='red',  marker='D', facecolor='white', zorder=3)
# 绘点函数scatter(水平坐标，垂直坐标),绘点函数
# zorder渲染顺序，具体的图形层，如果三层就输入3，余弦一层，正弦一层，这样就将点绘制在正弦和余弦图上面
# marker确定点的形状
# edgecolor 勾边颜色
# facecolor 绘画出点的填充颜色
# s = 大小

mp.annotate(r'$sin(\frac{3\pi}{4}=\frac{\sqrt{2}}{2})$',
            xy=(xo, yo_sin), xycoords='data', xytext=(20, 20),
            textcoords='offset points',	fontsize=14, arrowprops=dict(
                arrowstyle='->', connectionstyle='arc3, rad=0.2'))

mp.annotate(r'$\frac{1}{2}cos(\frac{3\pi}{4}=\frac{\sqrt{2}}{2})$',
            xy=(xo, yo_cos), xycoords='data', xytext=(-90, -40),
            textcoords='offset points',	fontsize=14, arrowprops=dict(
                arrowstyle='->', connectionstyle='arc3, rad=0.2'))


# annotate注释文本
# sqrt平方根
# frac{\sqrt{2}}{2}=二分之根号二,
# xy=被注释点的纵坐标(数据/图形的垂直坐标,数据/图形水平坐标)
# xycoords=被注释坐标属性（描述data数据或其他）
# xytetx=文字的水平和垂直(水平偏移多少,垂直偏移多少 )
# textcoords=设定文本是一个什么形式的坐标，'offset points' 自动偏移位
# fontsize字体大小
# arrowprops=dict(arrowstyle='->')#设置普通箭头
# connectionstyle#指定连接风格'arc3(圆弧)，rad=0.2(半径)'
# 图形对象
# mp.figure(图型名)显示在图形标题栏的文本，同时也代表着这个图形对象，可以在figure这个图形对象创建后重新获取
# 可以添加facecolor 背景颜色,figsize(图的宽，高单位是英寸)，dpi=num英寸的点数
# mp.title('图的标题',fontsize=字体大小)


mp.xlabel('x', fontsize=15, color='red')  # 标识坐标x
mp.ylabel('y', fontsize=15, color='red')  # 标识坐标y
mp.tick_params(labelsize=10)  # 设置坐标轴刻度标签大小
mp.grid(linestyle=':')  # 设置网格线和网格线型
mp.legend(loc='upper left')  # 显示标签 如果设置为空
mp.show()  # 显示图形
