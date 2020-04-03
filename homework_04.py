import requests
import time
import json
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import  MultipleLocator
# 数据爬取
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_=%d' %int(time.time() * 1000)
# 得到纯文本信息
response = requests.get(url)
# 数据解析，获取data
data = response.json()['data']
# 将data_dict转为字典
data_dict = json.loads(data)

day_list = []
nowconfirm_list = []
heal_list = []
dead_list = []

hubei_day_list = data_dict['dailyHistory']

for item in hubei_day_list:
    month, day = item['date'].split('.')
    date = '2020-%s-%s' %(month,day)
    # strptime: 把字符串转换成 datetime
    date_format = datetime.strptime(date, '%Y-%m-%d')
    day_list.append(date_format)
    nowconfirm_list.append(item['hubei']['nowConfirm'])
    heal_list.append(item['hubei']['heal'])
    dead_list.append(item['hubei']['dead'])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(day_list[::5], nowconfirm_list[::5], color='red',  marker='o', mfc='white', label='现有确诊')
plt.plot(day_list[::5], heal_list[::5], color='green', marker='o', mfc='white', label='累计治愈')
plt.plot(day_list[::5], dead_list[::5], color='grey', marker='o', mfc='white', label='累计死亡')

plt.xticks(rotation=60)
plt.title('湖北确诊/治愈/死亡趋势')
plt.legend(loc = 'upper left')
# 设置间隔为5
location = MultipleLocator(5)
ax=plt.gca()
ax.xaxis.set_major_locator(location)
plt.grid(axis='y')
plt.show()


