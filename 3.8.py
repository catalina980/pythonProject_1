import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.sin(x)

plt.plot(x, y)

ax = plt.gca()

# 把两个轴线隐藏起来
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 关键
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 有没有都可
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show();

# 3.9 直方图
# plt.hist()
# bins 几个矩形
# hisstyle 堆叠直方图 或者 bottom = y
# orientation 水平直方图或者垂直

# 3.10 绘制误差条
# 例 直方图 bar(x,y yerr = xe,width=0.4,align = 'center',ecolor = 'r')

# 3.11 绘制饼图
# 分裂式饼图
labels = 'Spring','Summer','Autumn','Winter'
x=[15,30,45,10]
explode = (0.1,0.1,0.1,0.1)
plt.pie(x,explode=explode,labels=labels,autopct='%1.1f%%',startangle=67)
plt.show();

# 3.12 绘制带填充区域的图表
# ax = plt.gca()
# ax.plot(x,y1,x,y2,color='black')
# ax.fill_between(x,y1,y2,where=y1>=y2,facecolor='darkblue',interpolate=True)

# 3.13 绘制带彩色标记的散点图
#plt.scatter(x,y,marker=,alpha=,edgecolors=,labels=)
# 点状标记，默认circle  透明度 标记的边界颜色  用于图例框