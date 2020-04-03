import requests
import time
import json
from datetime import datetime
import matplotlib.pyplot as plt
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_=%d' %int(time.time() * 1000)
response = requests.get(url)
data = response.json()['data']
data_dict = json.loads(data)

day_list = []
confirm_list = []
heal_list = []
dead_list = []
china_day_list = data_dict['chinaDayList']
for item in china_day_list:
    #将字符串转换为datetime对象
    #strptim  将字符串转换
    #需要添加年
    month, day = item['date'].split('.')
    date = '2020-%s-%s' %(month,day)
    date_format = datetime.strptime(date, '%Y-%m-%d')

    #print(item['date'])
    #print('confirm', item['confirm'])
    #print('heal', item['heal'])
    #day_list.append(item['date'])
    day_list.append(date_format)
    confirm_list.append(item['confirm'])
    heal_list.append(item['heal'])
    dead_list.append(item['dead'])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(day_list, confirm_list, color='red', marker='.', label='确诊')
plt.plot(day_list, heal_list, color='green', label='治愈')
plt.plot(day_list, dead_list, color='grey', label='死亡')
plt.xticks(rotation=-60)
#显示图例 指定位置
plt.legend(loc = 'upper left')
#显示图网虚拟网格
plt.grid(linestyle=':')

plt.show()

