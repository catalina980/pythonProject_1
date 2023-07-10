import matplotlib as mpl
import numpy as np
import datetime as d
import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.gca()

start = d.datetime(2013,1,1)
stop = d.datetime(2013,12,31)
delta = d.timedelta(days = 1)

dates = mpl.dates.drange(start,stop,delta)

values = np.random.rand(len(dates))
# 随机生成0-1均匀分布的几个数
# randn 是标准正态分布
# normal 是均值、标准差、数量

ax.plot_date(dates,values,linestyle = '-',marker = ' ')

date_format = mpl.dates.DateFormatter('%Y-%m-%d')

ax.xaxis.set_major_formatter(date_format)
# 主刻度
# 额外的格式还有 mpl.ticker.FormatStrFormatter mpl.ticker.MultipleLocator(10)

fig.autofmt_xdate()

plt.show()
