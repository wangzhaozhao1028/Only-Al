#coding=utf-8
import matplotlib.pyplot as plt 
import marplotlib.gridspec as gridspec

'''设置坐标轴 分格显示
'''
# method 1 
# plt.figure()

# ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# ax1.plot([1,2],[1,2])
# ax1.set_title('ax1_title')
# plt.xlim()
# ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,)
# ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2,)
# ax4 = plt.subplot2grid((3,3),(2,0))
# ax5 = plt.subplot2grid((3,3),(2,1))

# method2
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax1 = plt.subplot(gs[1:,2])
ax1 = plt.subplot(gs[-1,0])
ax1 = plt.subplot(gs[-1,-2])



plt.tight_layout()
plt.show()