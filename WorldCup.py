import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# 加载数据
hist_worldcup = pd.read_csv("WorldCupsSummary.csv")
pd.set_option("display.width", 1000)
pd.set_option("display.max_column", None)

# 数据预处理
hist_worldcup = hist_worldcup.replace('[Germany FR]', 'Germany')
print(hist_worldcup)
print(hist_worldcup.dtypes)
# 包括必要的数据类型转换

# 历年现场观众人数变化趋势
# 绘制全局绘图参数
# 散点图
font = {
    'weight': 'bold',
    'size': '20'
}
plt.rc('font', **font)
fig,ax = plt.subplots(figsize=(12, 8))
plt.title("Attendance Number")
hist_worldcup.plot.scatter(x='Attendance', y='Year', ax=ax, zorder=2, s=100)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_xticks([500000, 1000000, 1500000, 2000000,
              2500000, 3000000, 3500000, 4000000])
ax.set_yticks(hist_worldcup['Year'].tolist())
ax.ticklabel_format(style='plain')
plt.tick_params(bottom=False, left=False)
plt.show()