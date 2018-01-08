#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''设置坐标轴 图像
'''
a = np.array([0.31366, 0.36534, 0.42377,
	         0.36534, 0.43959, 0.63608,
	         0.42373, 0.52508, 0.65153]).reshape(3,3)

plt.imshow(a, interpolation='nearest', cmap='bone',origin='upper')
#侧边描述,可压缩
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()