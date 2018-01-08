#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''设置坐标轴 散点数据
'''
n = 1024

X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
# 颜色表示
T = np.arctan2(Y,X)
# alpha 透明度. cmap 可以自定义
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
# 一条线上的散点
# plt.scatter(np.arange(5), np.arange(5))

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
# 隐藏x,y轴的坐标值
plt.xticks(())
plt.yticks(())
plt.show()