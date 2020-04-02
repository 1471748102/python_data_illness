import requests
import time
import json
import matplotlib.pyplot as plt
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' %int(time.time() * 1000)
response = requests.get(url)
response_json = response.json()
data = response_json['data']
data_dict = json.loads(data)
province_list = data_dict['areaTree'][0]['children']
print(province_list)
province_name = []
province_confirm = []
count = 0
for province in province_list:
    province_name.append(province['name'])
    province_confirm.append(province['total']['confirm'])
    count += 1
    if count == 10:
        break
print(province_name)
print(province_confirm)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(province_name, province_confirm, color='red')
plt.xticks(rotation=-60)
plt.xlabel('省份')
plt.ylabel('确诊人数')
plt.title('各个省份确诊人数')
plt.show()