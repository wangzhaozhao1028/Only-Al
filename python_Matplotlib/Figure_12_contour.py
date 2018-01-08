#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''设置坐标轴 等高线
'''
def f(x,y):
    return (1-x/2 + x**5 + y**3) * np.exp(-x**2 -y**2)

# x.y都有256个点,正方形
n=256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x,y)

# X.Y 构建成一个网格

#放颜色
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

# 等高线的线  8,把等高线等分多少份,10个圈
C = plt.contour(X,Y,f(X,Y),8, colors='black', linewidth=.5)

# 数字描述,True 决定线条要不要穿过数字
plt.clabel(C,inline=True,fontsize=10)
plt.xticks(())
plt.yticks(())
plt.show()