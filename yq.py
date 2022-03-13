import re, csv, os

import numpy as np
import pandas as pd

data = []
f2 = open("yq_in_13.csv", "w")
with open("yq_in_03.txt", "r") as f1:
    for i in f1:
        line = re.split('\s+', i)  # 将字符串i以全部空白字符为分割符，将其分割成一个字符列表
        new_line = ','.join(line)  # 将字符列表用','拼接成一个新字符串
        new_line = new_line.strip(',')  # 将新字符串尾部产生的','去掉
        new_line = new_line + '\n'
        print(new_line)
        data.append(new_line)
    print(data)
    m = len(data)
    for j in range(0,m):
        f2.write(data[j])
f2.close()
df = pd.read_csv('yq_in_13.csv', encoding='gb2312')  # 如果没有encoding='gb2312'，会出现写入乱码
df = np.array(df)
print(df)
print(len(df))

data1 = []
y=0
f3 = open("yq_out_03.txt", "w")
for i in range(0,len(df)-1):
    y=y+1
    if df[i+1][0]!=df[i][0] or i+1==len(df)-1:
        data1.append(df[i][0])
        data1.append('\n')
        for j in range(i+1-y,i+1):
            data1.append(df[j][1])
            data1.append('      ')
            data1.append(df[j][2])
            data1.append('\n')
            y=0
print(data1)
n = len(data1)
for j in range(m):
    f3.write(str(data1[j]))
f3.close()
