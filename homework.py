# 作业一

age = 60
appearance = 50
money = 7000000

if(age <25 and appearance>90 and money>1000000):
    print('我要嫁给你')
if(age <25 or appearance>90 or money>1000000):
    print('哎，嫁了吧')
else:
    print('不嫁！')


# 作业二

yase_life = 150
yase_attack = 12
ake_life = 100
ake_attack = 15

while yase_life>0 and ake_life>0 :
    yase_life = yase_life-ake_attack
    # print('yase',yase_life)
    ake_life = ake_life-yase_attack
    # print('ake',ake_life)
if(yase_life<=0 and ake_life<=0):
    print('同归于尽！')
if(ake_life<=0):
    print('亚瑟胜利！')
if(yase_life<=0):
    print('阿珂胜利！')


# 作业三

starts = '王一博 李现 杨紫 肖战 易烊千玺 关晓彤 李现 杨紫 肖战 易烊千玺 王一博 关晓彤 肖战 李现'
names = starts.split(' ')
count = 0
for name in names:
    if name == '肖战':
        count = count +1
print(count)



# 作业四
infos = {'哈登':'123456', '詹姆斯':'456789', '字母哥':'666666'}
username = input("请输入用户名：")
password = input('请输入密码：')
if not infos.get(username):
    print('用户不存在')
else:
    if infos.get(username) == password:
        print('登录成功！')
if infos.get(username):
    if not infos.get(username) == password:
        print('密码不正确！')


