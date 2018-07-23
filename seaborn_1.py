# -*- coding: utf-8 -*-
"""
@author: tz_zs

FacetGrid 用于按指定的分类画出多个子图
"""
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style="ticks")
np.random.seed(sum(map(ord, "axis_grids")))

tips = sns.load_dataset("tips")
tips.head()

g = sns.FacetGrid(tips, col="time")
g.map(plt.hist, "tip")

g = sns.FacetGrid(tips, col="sex", hue="smoker")  # 按sex，分成不同列的子图，按smoker用不同的表现颜色
g.map(plt.scatter, "total_bill", "tip", alpha=.7)
g.add_legend()  # 添加图例

g = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)  # 用smoker的不同分行，time的不同分列
g.map(sns.regplot, "size", "total_bill", color=".1", fit_reg=False, x_jitter=.1)
