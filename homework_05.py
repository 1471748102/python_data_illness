import numpy as np
import pandas as pd
# 作业一

npa = np.linspace(0, 1, 12)
print(npa)

# 作业二
npb = np.asarray(range(0, 10))
print(npb)

# 作业三
npc = np.arange(10, 50)
print(npc)

# 作业四
data = {'性别': ['男', '女', '女', '男', '男'],
        '姓名': ['小明', '小红', '小芳', '大黑', '张三'],
        '年龄': [20, 21, 25, 24, 29]
        }
df = pd.DataFrame(data)
print(df.iloc[:, 1])
print(df.iloc[0:2, :])

