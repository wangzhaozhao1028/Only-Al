#coding=utf-8
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation


'''设置坐标轴 动画展示
'''
fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi,0.01)
line, = ax.plot(x, np.sin(x))
# 动画效果 init_func 开始的时候什么样,interval 频率
# 自定义func
def animate(i):
	line.set_ydata(np.sin(x+i/10))
	return line,

def init():
	line.set_ydata(np.sin(x))
	return line,


ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=False)
plt.show()