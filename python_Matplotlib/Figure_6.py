##coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''设置坐标轴
'''
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
#linewidth 粗度, linestyle虚线
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

#取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#x,y 描述
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
# print(new_ticks)
plt.xticks(new_ticks)
#r 和$ 为了字体好看 阿尔法 表示 \alpha
plt.yticks([-2,-1.8,-1,1.22,3,],
	[r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
ax = plt.gca()
#x,y的上边框和右边框去掉实线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# x,y轴移动
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


ax.spines['bottom'].set_position(('data',-1))    #outward,axes
ax.spines['left'].set_position(('data',0))

plt.show()