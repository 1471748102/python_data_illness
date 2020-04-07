import pandas as pd
import numpy as np

# 带上索引index+value
a = pd.Series([1,2,3,4])
print(a)

# DataFrame
d = {'col1':[1,2],'col2':[3,4]}
e = pd.DataFrame(d)
print(e)

df2 = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=['a','b','c'])
print(df2)

# df3 = pd.read_csv()   ,
# df3 = pd.read_table()   \t
# 获取行索引：(df3.index)
# 获取列索引 (df3.columns)
# 查看前十行  df.head(10)
# 查看尾十行  df.tail(10
# iloc(index)) 通过index定位 类似于切片   df3.iloc[0:2]  df3.iloc[0:2,0:2],df3.iloc[:,0:2]
# loc通过label定位  df3.ioc[:,'城市']

# 删除操作  df.drop(['类型','人数'],axis = 1，inplace = False)  行 0  列 1  是否在原表删除
