# -*- coding: utf-8 -*-
"""
@author: tz_zs
@file: draw.py
@time: 2018/7/18 0:50
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 100)
y1 = np.random.randint(20, 60, size=100)
y2 = np.random.randint(30, 70, size=100)
y3 = np.random.randint(50, 90, size=100)

plt.figure(num="111", figsize=(6, 4), facecolor="pink", edgecolor="green")
plt.plot(x, y1, c="red", label="y1_low")
plt.plot(x, y2, c="blue", label="y2_middle")
plt.plot(x, y3, c="yellow", label="y3_high")
plt.legend(loc="best")
plt.show()
