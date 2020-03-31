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
print(dict.get('sunwukong',150))
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