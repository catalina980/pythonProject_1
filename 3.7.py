import numpy as np
import matplotlib.pyplot as plt

x1=np.random.normal(30,3,100)
x2=np.random.normal(20,2,100)
x3=np.random.normal(10,3,100)

plt.plot(x1,label = 'plot')
plt.plot(x2,label = '2nd plot')
plt.plot(x3,label = 'last plot')

plt.legend(bbox_to_anchor=(0.,1.02,1.,.102),loc = 1,ncol=3,mode="expand",borderaxespad=0.)
#标签 起始位置 宽 高 图例框的位置，用数字表示 列数 扩展至整个坐标轴区域 坐标轴与图例之间的距离
#plt.annotate("Important Value",(55,20),xycoords='data',xytext=(5,38),arrowprops=dict(arrowstyle='->'))

plt.show()
