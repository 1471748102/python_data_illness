import numpy as np
import requests
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
import datetime as dt

# parameter_K、parameter_r 是需要后面确定
# 60000 ~ 200000
parameter_k = None
# 0 ~ 1
parameter_r = None


def logistic_function(t, P0):
    exp_r = np.exp(parameter_r * t)
    return parameter_k * P0 * exp_r / (parameter_k + P0 * (exp_r - 1))


url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'

x_data_date = []
y_data = []
x_data = []
response = requests.get(url)
usa_day_list2 = response.json()['data']


# 1、获取历史数据：确诊人数数据
def history_data(usa_day_list):
    x_data_date2 = []
    y_data2 = []

    for item in usa_day_list:
        y_data2.append(item['confirm'])
        x_data_date2.append(item['date'])

    # 可不可以是字符串？不可以！整数
    x_data2 = np.arange(0, len(y_data2))

    print('y_data长度为:', len(y_data2))
    print('x_data2: ', x_data2)
    print('y_data2: ', y_data2)
    return x_data_date2, x_data2, y_data2


# 2、通过获取的确诊数据，进行拟合，求出Logistic方程中的参数
def view_list(x_data3, y_data3):
    # 遍历K的区间和r的区间
    K_range = np.arange(460000, 1000000, 1000)
    r_range = np.arange(0, 1, 0.01)
    # 表示一个正无穷大数
    loss = float('inf')
    optimal_K = None
    optimal_r = None
    optimal_P0 = None
    i = 0

    def logistic_function(t, P0):
        exp_r = np.exp(parameter_r * t)
        return parameter_k * P0 * exp_r / (parameter_k + P0 * (exp_r - 1))

    for K_ in K_range:
        for r_ in r_range:
            parameter_k = K_
            parameter_r = r_

            popt, pcov = curve_fit(logistic_function, x_data3, y_data3)
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
                optimal_k = K_
                optimal_r = r_
                optimal_P0 = popt

            i += 1
            # 拟合进度：▉▉▉▉42%        
            print('\r拟合进度：{0}{1}%'.format('▉' * int(10 * i / len(K_range) / len(r_range)),
                                          int(100 * i / len(K_range) / len(r_range))), end='')
    print('\noptimal_K: ', optimal_K)
    print('optimal_r: ', optimal_r)
    print('optimal_P0: ', optimal_P0)
    parameter_k = optimal_k
    parameter_r = optimal_r
    return optimal_P0, parameter_k, parameter_r


# 3、进行预测，把未来的天数输入到预测模型中，获取天数对应的预测确诊数
def predict_data(optimal_P02):
    # 预测日期，从第一天到第100天，截止到4月10日，美国疫情开始第74天。可以预测后面的26天的发展趋势
    x_data_predict = np.arange(0, 100)
    y_data_predict = logistic_function(x_data_predict, optimal_P02)
    # 去掉小数点
    y_data_predict = y_data_predict.astype('int64')
    print('y_data_predict: ', y_data_predict)
    return y_data_predict


# 4、可视化
def look_data(y_data_predict, x_data_date, usa_day_list):
    # 获取第一天
    month, day = usa_day_list[0]['date'].split('.')
    # 2020-01-28 字符串 转成 datetime
    first_date = dt.datetime.strptime('2020-' + month + '-' + day, '%Y-%m-%d')
    x_data_predict_date = [(first_date + (dt.timedelta(days=i))).strftime("%m.%d") for i in range(100)]

    # 解决中文乱码的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 指定画布大小
    plt.figure(figsize=(12, 6), dpi=300)
    # 预测确诊，注意：横坐标列表长度 要和 纵坐标列表长度 一致
    plt.plot(x_data_predict_date, y_data_predict, linewidth='1.5', color='red', label='预测确诊')
    # 现实确诊
    plt.scatter(x_data_date, y_data, s=35, color='dimgrey', label='实际确诊')

    # 显示图例，指定位置，防止图片被覆盖
    plt.legend(loc='upper left')
    plt.xticks(rotation=60)

    # 显示网格
    plt.grid()
    plt.ylabel('确诊人数')
    plt.savefig('usa_predict.png', dpi=300)
    plt.show()


# 第一步
x_data_date, x_data, y_data = history_data(usa_day_list2)
# 第二步
optimal_P0, parameter_k, parameter_r = view_list(x_data, y_data)
# 第三步
y_data_predict2 = predict_data(optimal_P0)
# 第四步
look_data(y_data_predict2, x_data_date, usa_day_list2)

