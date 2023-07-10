import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyecharts.charts as pyc
import pyecharts.options as opts
import warnings
warnings.filterwarnings("ignore")

# 加载数据
df_baby = pd.read_csv("tianchi_mum_baby.csv")
df_trade = pd.read_csv("tianchi_mum_baby_trade_history .csv")

# 数据预处理
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df_trade.head())
print(df_trade.dtypes)
# 先将int转化为str，再转化为时间
df_trade["day"] = pd.to_datetime(df_trade.day.astype("str"))
print(df_trade.head())
df_trade["year"] = df_trade.day.dt.year
df_trade["quarter"] = df_trade.day.dt.quarter
df_trade["month"] = df_trade.day.dt.month
print(df_trade.head())
print(df_trade.day.describe())
print(df_trade.buy_mount.describe())
df_trade = df_trade[(df_trade.buy_mount >= 1) & (df_trade.buy_mount <= 189)]
print(df_trade.buy_mount.describe())

count_user = df_trade.user_id.nunique()
count_auction = df_trade.auction_id.nunique()
count_category_1 = df_trade.category_1.nunique()
count_category_2 = df_trade.category_2.nunique()
count_buy_mount = df_trade.buy_mount.sum()
print("用户数", count_user)
print("交易数", count_auction)
print("商品一级类目数", count_category_1)
print("商品二级类目数", count_category_2)
print("总销量：", count_buy_mount)

print(df_baby.head())
print(df_baby.count())
df_baby = df_baby[(df_baby != 2)]
print(df_baby.count())
print(df_baby.dtypes)
df_baby["birthday"] = pd.to_datetime(df_baby.birthday.astype("str"))
print(df_baby.birthday.describe())
df_baby = df_baby[(df_baby.birthday > '2010-01-01')]
print(df_baby.birthday.describe())

# 流量分析
print(df_trade.head())
# 根据年月查看销量趋势
# year_states = df_trade.groupby(by='year')['buy_mount'].sum()
# plt.figure(figsize=(10,5))
# sns.barplot(x=year_states.index,y=year_states.values) ##直方图
# plt.title("Sales Volume By Year")
# plt.xlabel("Year")
# plt.ylabel("Sales Volumn")
# plt.show();

# 各年季度销量情况
# year_quarter_states = df_trade.groupby(by = ['year','quarter'])['buy_mount'].sum()
# print(year_quarter_states)
# x_list = [str(idx[0]) + "/Q" + str(idx[1]) for idx in year_quarter_states.index]
# y_list = [int(value) for value in year_quarter_states.values]
# plt.figure(figsize=(10,5))  ##plt在前，直方图在后
# sns.barplot(x=x_list,y=y_list)
# plt.title("Sales Volume By Year-Season")
# plt.xlabel("(Year,Season)")
# plt.ylabel("Sales Volumn")
# plt.show();

# 根据年月分组
# year_month_states = df_trade.groupby(by = ['year','month'])['buy_mount'].sum()
# x_list = [str(idx[0]) + "/" + str(idx[1]) for idx in year_month_states.index]
# y_list = [int(value) for value in year_month_states.values]
# plt.figure(figsize=(30,5))
# sns.barplot(x=x_list,y=y_list)
# plt.title("Sales Volume By Year-Month")
# plt.xlabel("(Year,Month)")
# plt.ylabel("Sales Volumn")
# plt.show();

# 以2014年11月份为例
# df_trade_201411 = df_trade[(df_trade.day >= '2014-11-01') & (df_trade.day <= '2014-11-30')]
# print(df_trade_201411.head())
# day_states = df_trade_201411.groupby(by='day')['buy_mount'].sum()
# print(day_states)
# x_list = [str(idx.month) + "-" + str(idx.day) for idx in day_states.index]
# y_list = [int(value) for value in day_states.values] #x,y格式一致
# plt.figure(figsize=(50,5))
# sns.barplot(x=x_list,y=y_list)
# plt.title("Sales Volume By Day(2014/11)")
# plt.xlabel("Date",fontsize = 11)
# plt.ylabel("Sales Volumn")
# plt.show();

# 商品大类销售情况
# category_1_stats = df_trade.groupby(by='category_1')['buy_mount'].sum()
# plt.figure(figsize=(10,5))
# sns.barplot(x=category_1_stats.index,y=category_1_stats.values)
# plt.title("Sales Volume By Category_1")
# plt.xlabel("Category_1")
# plt.ylabel("Sales Volumn")
# plt.show();

# 一级类目下二级类别数量
# category_2_stats = df_trade.groupby(by='category_1')['category_2'].nunique()
# plt.figure(figsize=(10,5))
# sns.barplot(x=category_2_stats.index,y=category_2_stats.values)
# plt.title("Category_2_stats")
# plt.xlabel("Category_1")
# plt.ylabel("Unique Number of Category_2")
# plt.show();

# 人均大类下购买情况，大类下每个子类的平均销售贡献
# ave_category_stats = (df_trade.groupby(by='category_1')['buy_mount'].sum()) / (df_trade.groupby(by='category_1')['category_2'].nunique())
# sns.barplot(x=ave_category_stats.index, y=ave_category_stats.values)
# plt.title("Average Sales Volumn Stats by Category_2")
# plt.xlabel("Category_1")
# plt.ylabel("# Avg Contribution of Category_2")
# plt.show()

# 性别分析
df_merge = pd.merge(df_trade, df_baby)
# print(df_merge.head())
df_merge['age'] = round(
    (df_merge['day'] -
     df_merge['birthday']) /
    pd.Timedelta(
        days=365),
    2)
# print(df_merge.head())
df_merge = df_merge[df_merge.age > 0]
# print(df_merge.age.describe())

# 计算比例函数


def computer_fraction(pct, allvals):
    absolute = int(pct / 100 * np.sum(allvals))  # 被调用
    return '{:.2f}%\n{:d}'.format(pct, absolute)
# 统计性别比例
# gender_stats_by_user = df_merge.groupby(by="gender")["user_id"].count()
# labels = ['boy','girl']
# values = np.array([gender_stats_by_user[0],gender_stats_by_user[1]])
# print(values)
# fig = plt.figure()
# sub = fig.add_subplot(111)  #子图，同时显示，进行对比
# sub.pie(values,labels=labels,startangle = 90,autopct = lambda x:computer_fraction(x,values))
# # startangle：饼块起始角度 ;startangle：饼块起始角度 ; startangle：饼块起始角度
# sub.legend()
# fig.suptitle("Gender Stats by User",fontsize = 16)
# fig.tight_layout()
# plt.show()


# 性别在商品大类中的表现
gender_stats_by_buy_mount = df_merge.groupby(
    by=['gender', 'category_1'])['buy_mount'].sum()
print(gender_stats_by_buy_mount)
category_1_list = [28, 38, 50008168, 50014815, 50022520, 122650008]
# 男孩的类别销售统计
values = np.array([gender_stats_by_buy_mount.loc[0, category]
                  for category in category_1_list])
fig = plt.figure()
sub = fig.add_subplot(111)
sub.pie(values, labels=category_1_list, startangle=90,
        autopct=lambda x: computer_fraction(x, values))
fig.suptitle('Sales Volumn by Boy')
plt.show()
