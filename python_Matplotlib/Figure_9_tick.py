#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''设置坐标轴 能见度
'''
x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
# 实线
plt.plot(x, y,)
#虚线
# plt.scatter(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for lable in ax.get_xticklabels() + ax.get_yticklabels():
	lable.set_fontsize(12)
	lable.set_bbox(dict(facecolor='white', edgecolor='None',alpha=0.7))

plt.show()