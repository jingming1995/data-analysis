# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 10).reshape(3, 3).astype(float)
# print(a)
a[1][1] *= 10
print(a.reshape(3, 3))
