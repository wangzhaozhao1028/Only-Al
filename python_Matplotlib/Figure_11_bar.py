#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''设置坐标轴 柱状图
'''
# 12个柱状图
n = 12
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0,n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

# 柱状图颜色表示#9999ff
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
	# ha: 对齐方式
	plt.text(x + 0.4, y + 0.05, '%.2f' %y, ha='center', va='bottom')


for x,y in zip(X,Y2):
	# ha: 对齐方式
	plt.text(x + 0.4, -y - 0.05, '-%.2f' %y, ha='center', va='top')


plt.xlim((-.5,n))
plt.xticks(())

plt.ylim((-1.25,1.25))
# 隐藏x,y轴的坐标值
plt.yticks(())

plt.show()