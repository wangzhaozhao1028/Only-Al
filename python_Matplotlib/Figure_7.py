##coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''设置坐标轴 图例Legend
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

h1, = plt.plot(x,y2,label='up')
h2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')

plt.legend()


plt.show()