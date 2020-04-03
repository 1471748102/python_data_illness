# 数据可视化库 matplotlib
# 折线图 散点图 饼状图
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
x_list = ['4.1', '4.2', '4.3']
y_list = [1000,2000,3000]
# 加上 b 颜色蓝色  o 圆圈大小
#plt.plot(x_list, y_list, 'bo')
# scatter 设置大小 散点样式 颜色
#plt.scatter(x_list, y_list, s=35, marker='.', c='dimgray')
# 饼状图
# 指定切片大小，每个切片名字
slices = [10000, 3000, 500, 100]
activities = ['hubei', 'henan', 'guangdong', 'zhejiang']
colors = ['y', 'g', 'b', 'r']
plt.pie(
    slices,
    labels=activities,
    colors=colors,
    #图形开始启动角度
    startangle=90,
    # 设置一个阴影
    shadow=True,
    # 拉出一个切片
    explode=(0,0.1,0,0),
    # 在图中显示占比
    autopct='%1.2f%%'
)
#plt.show()