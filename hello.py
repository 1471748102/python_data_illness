print("hello -----")
# 2.39*10三次方
x = 2.39e3
hello = 50
height = 150.5
print(hello)
print(height)
print(x)

lol = '英雄联盟'
print(lol)
lol = 12
print(lol)
a = 10
b = 12


# 流程控制 代码块
if a and b:
    print("manzu")
age = 20
if age <28:
    print("xiaoxianrou")
else:
    print("laolarou")
i=12
if i<20:
    print('小于20')
    if i<15:
        print('小于15')

# for循环  range stop step
for i in range(1,10,2):
    print(i)

elec = 10
while elec > 0:
    print(elec)
    elec = elec -1
    if elec == 5:
        continue
    print("hello")



age =20
name = '亚瑟'
print('我今年%d岁' % age)
print('age: %d name: %s' %(age,name))
print("年龄是",age,"名字是",name)

# str = input("请输入：")
# si = int(str)
# print("shurudeshi",str)

# 字符串操作 split replace strip(不包括内部的空格)
url  = 'www.bilibili.com'
aurl = url.split('.')
print(aurl)

burl = url.replace('b','c')
print(burl)

# curl = url.strip()

# 列表  增删改查
names = ['libiai','zhangfei','guanyu']
lists = [1,1.5,names]
print(lists)

names.append('sunwukong')
print(names)
names.insert(1,'hanxin')
print(names)
names.pop()
print(names)
names[0] = 'libaigai'
print(names)
for name in names:
    print(name)

# 字典 类似于map
dict = {'luban':100,'daji':120}
print(dict['luban'])
# 如果不存在 返回NONE  或者默认值
print(dict.get('luban1'))
print(dict.get('sunwukong','morenzhi'))
dict['sunwukong'] = 150
print(dict)

dict.pop('sunwukong')
print(dict)

dict['luban'] = 500
print(dict['luban'])

for i in dict.items():
    print(i)
for i in dict.keys():
        print(i)
for i in dict.values():
    print(i)


dicta = {}
dicta['haha'] = 1
print(dicta)

#元组　不能修改增加删除
t = (10,20,30)
print(t[0])
# set  不允许重复        空的set空的字典
seta = {1,2,3,2,3}
print(seta)
seta.add(6)
print(seta)
seta.remove(6)
print(seta)


# 函数  默认值修改时 加上参数名
def count(i):
    i=i+1
    return i
    print(i)
result = count(1)
print(result)
count(3)

# 模块 导入使用，也可以导入函数使用
import time
print('要睡了')
time.sleep(0.1)
print('睡好了')

# 文件读写  打开 读取 关闭
# open(file mode = 'r' encoding=None)
file = open('G:\login.txt', 'r', encoding='utf8')
print(file.read())
with open('G:\login.txt', 'w', encoding='utf8') as files:
    files.write('覆盖le')  # w覆盖写  a追加写
files.close()
filess = open('G:\login.txt', 'r', encoding='utf8')
print(file.readline().strip())

# 爬虫基础
import requests
import time
url = 'https://www.baidu.com'
response = requests.get(url)
response.encoding = 'utf8'
#print(response.text)


urla = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' %int(time.time() * 1000)
response = requests.get(urla)
print('输出JSON格式下的data里面的数据：')
print(response.json()['data'])
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' %int(time.time() * 1000)
response = requests.get(url)
print('输出text格式和JSON格式：')
print(response.text)
print(response.json())
# data 是字符串
response_json = response.json()
data = response_json['data']
print('再输出一次JSON格式下的data里面的数据：')
print(data)

# 目标 获取河南省下所有城市的疫情数据
# data是字符串 获取数据不太方便  转换成dict
import json
data_dict = json.loads(data)
print('转换为字典格式')
print(data_dict)
# 1,获取省份的列表
province_list = data_dict['areaTree'][0]['children']
print(province_list)
# 2.找到河南这个省份
henan_cities = []
for province in province_list:
    if province['name'] =='河南':
        henan_cities=province['children']
print('河南省内的所有城市：')
for city in henan_cities:
    print(city)

#获取所有省份的名字以及对应的确诊信息

#获取所有城市的名字以及对应的确诊信息
import matplotlib.pyplot as plt
cities_name = []
cities_confirm = []
for city in henan_cities:
    cities_name.append(city['name'])
    cities_confirm.append(city['total']['confirm'])
# 可视化展示
#解决中文乱码的问题
plt.rcParams['font.sans-serif'] = ['SimHei']

#条形图 第一个是横坐标 城市名字
plt.bar(cities_name,cities_confirm, color='red')

#横坐标字体重叠
#第一种 颠倒横坐标
# plt.bar(cities_confirm,cities_name)
#第二种：旋转城市字体
plt.xticks(rotation=-60)
plt.xlabel('城市')
plt.ylabel('确诊人数')
plt.title('河南省各城市确诊人数')
plt.show()