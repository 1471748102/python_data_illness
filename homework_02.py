

# 作业一
def getmax(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2


num1 = int(input('请输入一个整数：'))
num2 = int(input('请输入另一个整数：'))
print('这两个数比较大的是：',getmax(num1,num2))


# 作业二
def getright (num):
    if num>0:
        return num
    else:
        return -num


num = int(input('请输入一个整数：'))
print('这个数的绝对值是',getright(num))
