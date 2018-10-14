# -*- coding: utf-8 -*-
from __future__ import unicode_literals
数据分析

matlab
python

Numpy
1.Numrical python 数值是oython 应用于数值分析领域的python语言工具
2.Numpy 是一个开源的科学计算库
3.Numpy 弥补了作为通用编程语言的python在数值计算方面能力弱，速度慢的不足
4.Numpy拥有丰富的数学函数、强大的多维数组和优异的运算性能
5.Numpy与Scipy、scikit、matplotlib等其他科学计算库可以很好的协调工作
6.Numpy 可以取代matlab等工具，允许用户进行快速开发的同时完成交互式的原型设计
代码：vector.py

二、多维数组
1.numpy中的多维数组是numpy.ndarray类类型对象，可用于表示数据结构中的任意维度的数组
2.创建多维数组对象
numpy.arange(起始, 终止, 步长)->一维数组, 首元素就是起始值，尾元素为终止前的最后一个元素，
步长即每次递增的公差，缺省的起始值为0，缺省的步长为1。
numpy.array(任何可被解释为数组的容器)
3.内存连续、元素同质性
4.ndarray.drye属性表示元素的数据类型, 通过dtype参数和astype()方法可以修改制定元素
代码：array.py
5.ndarray.shape属性表示数组的维度：(高纬度数, ..., 低纬度数)
代码：aarray.py

6.元素索引
数组([索引])
数组([行索引][列索引])
数组([页索引][行索引][列索引])
数组([页索引, 行索引, 列索引])

7.numpy的内置类型和自定义类型

numpy的内置类型
bool_1字节布尔型
int8 1个字节有符号整型 - 128 - 127
int16 2个字节有符号整型
int32 4个字节有符号整型
int64 8个字节有符号整型

uint8 1个字节无符号整型 0 - 255
uint16 2个字节无符号整型
uint32 4个字节无符号整型
uint64 8个字节无符号整型

float16 2个字节有符号浮点型
float32 4个字节有符号浮点型
float64 8个字节有符号浮点型

complex64 8字节复数型
complex128 16字节复数型

str_字符串类型

自定义类型：通过dtype将多个相同或不同的numpy内置类型组合成复合类型，用于数组元素的数据类型
除了使用内置类型的全称以外还可以通过类型编码字符串简化类型的说明。

一个字节8个字节
