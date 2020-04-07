# 数学计算的库
import numpy as np

# 以往的思路
a = [1,2,3,4]
b = [1,2,3,4]
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
print(c)


# array
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
c = a * b
print(c)
print(c[0:3])

b = np.array([[1,2,3],[4,5,6]])
print(b)

# asarray
d = np.asarray(range(0, 10))
print(d)
d = np.asarray([1,2,3,4])
print(d)
# arange
c = np.arange(0,10,2)
print(c)
c = np.arange(10)
print(c)
# linspace
e = np.linspace(0, 10, 5)
print(e)

# 通函数
