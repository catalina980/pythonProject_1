import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-np.pi,np.pi,256,endpoint=True)
# endpoint 决定了终止值是否包含在结果数组中，缺省为true
# 参数分别为 start stop num dtype
# dtype 可以指定数据类型 int float
# num 表示生成几个数据

y=np.cos(x)
y1=np.sin(x)

plt.plot(x,y,linewidth = 1.5)
plt.plot(x,y1,linewidth = 4)
#改变线条宽度

plt.title("Function $\sin$ and $\cos$")
plt.xlim(-3.0,3.0)
plt.ylim(-1.0,1.0)

plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
# LaTex语法表示希腊字母
# '$ $'
plt.show()
