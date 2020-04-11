import json
import time
import numpy as np
import requests
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
# parameter_K、parameter_r 是需要后面确定
# 60000 ~ 200000
parameter_K = None
# 0 ~ 1
parameter_r = None
def logistic_function(t, P0):
    exp_r = np.exp(parameter_r * t)
    return parameter_K * P0 * exp_r / (parameter_K + P0 * (exp_r - 1))
# 1、获取历史数据：确诊人数数据
# 我们获取国内的历史数据，比如获取2月15日之前的数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_=%d' % int(time.time() * 1000)
response = requests.get(url)
data = response.json()['data']
print(data)
data_dict = json.loads(data)
day_list = []
y_data = []
# 这个处理是获取2月15日之前的数据，注意：这个处理可能在预测其他国家病例不太适用
count = 0
china_day_list = data_dict['chinaDayList']
for item in china_day_list:
    if count < 34:
        y_data.append(item['confirm'])
        count += 1
# 可不可以是字符串？不可以！整数
x_data = np.arange(0, len(y_data))
print('x_data: ', x_data)
print('y_data: ', y_data)
# 2、通过获取的确诊数据，进行拟合，求出Logistic方程中的参数
# 遍历K的区间和r的区间
K_range = np.arange(60000, 200000, 1000)
r_range = np.arange(0, 1, 0.01)
# 表示一个正无穷大数
loss = float('inf')
optimal_K = None
optimal_r = None
optimal_P0 = None
i = 0
for K_ in K_range:
    for r_ in r_range:
        parameter_K = K_
        parameter_r = r_
popt, pcov = curve_fit(logistic_function, x_data, y_data)
# 我们需要从这 len(K_range) * len(r_range) 循环次数中，
# 找出最优的一次（最优的K和最优的r），让logistic_function最符合预测
# 如何评判是最优的一次呢？
# 均方误差这个概念
# 讲解一下两个参数
# y_true:真实数据（疫情真实确诊人数）
# y_pred:预测数据（通过logistic_function函数返回的值）
loss_ = mean_squared_error(y_data, logistic_function(x_data, popt))
# 找到最小的 loss
if loss_ < loss:
    loss = loss_
    optimal_K = K_
    optimal_r = r_
    optimal_P0 = popt
i += 1
# 拟合进度：▉▉▉▉42%
print('\r拟合进度：{0}{1}%'.format('▉' * int(10 * i / len(K_range) /
len(r_range)),
int(100 * i / len(K_range) /
len(r_range))), end='')
print('optimal_K: ', optimal_K)
print('optimal_r: ', optimal_r)
print('optimal_P0: ', optimal_P0)
parameter_K = optimal_K
parameter_r = optimal_r
# 3、进行预测，把未来的天数输入到预测模型中，获取天数对应的预测确诊数
# 预测2月15日之后的确诊人数，再和现实数据进行对比，以此检验预测模型准不准可视化效果：
# 传的日期，可以是从第一天到最后一天
x_data_all = np.arange(0, len(china_day_list))
y_data_predict = logistic_function(x_data_all, optimal_P0)
y_data_predict = y_data_predict.astype('int64')
print('y_data_predict: ', y_data_predict)
# 4、可视化
# 02-11...
x_data_all_day = []
y_data_all_day = []
for item in china_day_list:
    x_data_all_day.append(item['date'])
    y_data_all_day.append(item['confirm'])
# 解决中文乱码的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 指定画布大小
plt.figure(figsize=(12, 6), dpi=300)
# 预测确诊
plt.plot(x_data_all_day, y_data_predict, linewidth='1.5', color='red', label='预测确诊')
# 现实确诊
plt.scatter(x_data_all_day, y_data_all_day, s=35, color='dimgrey', label='实际确诊')
# 显示图例，指定位置，防止图片被覆盖
plt.legend(loc='upper left')
plt.xticks(rotation=60)
# 显示网格
plt.grid()
plt.ylabel('确诊人数')
plt.show()