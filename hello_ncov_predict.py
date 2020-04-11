import datetime
import json
import time
import requests
import numpy as np
from scipy.optimize import curve_fit

# 60000~200000
parameter_K = None
# 0~1
parameter_r = None


def logistic(t, P0):
    exp_r = np.exp(parameter_r * t)
    return parameter_K * P0 * exp_r / (parameter_K + P0 * (exp_r - 1))
# 1. 获取历史数据 确诊人数数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_=%d' %int(time.time() * 1000)
response = requests.get(url)
data = response.json()['data']
data_dict = json.loads(data)
day_list = []
confirm_list = []

count = 0
china_day_list = data_dict['chinaDayList']
for item in china_day_list:
    if count < 34:
        confirm_list.append(item['confirm'])
        count += 1

# 2. 通过获取的确诊数据 进行拟合 求出logistic方程的参数
x_data = np.arange(0, len(confirm_list))
print('x_data:', x_data)
print('x_data::', confirm_list)

# 3. 预测 把未来的天数输入到预测模型中
k_range = np.arange(600000,200000,100)
r_range = np.arange(0,1,0.01)

loss = float('inf')

for k in k_range:
    for r in r_range:
        parameter_K = k
        parameter_r = r
        popt, pcov = curve_fit(logistic, x_data, confirm_list)
        print('popy:', popt)
        print('pocv', pcov)

#loss = mean_squared_error(confirm_list,logistic(x_data,popt))

# 4. 可视化
