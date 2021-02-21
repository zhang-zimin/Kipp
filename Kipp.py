import pandas as pd
import numpy as np
import plotly.graph_objects as go

data = pd.read_excel(r'E:\深圳项目\2020-12-15\Z32-1.xlsx',skiprows=11)
#载入xlsx数据，导入csv文件格式会报错；前面11行为无效信息，略过
data = data['LEVEL']
#只需要水位数据，剔除其余列
b=data.max()
#取水位最大值，一般为激发时的水位
intri_index = int(np.where(data==b)[0])
start_index = intri_index -10
#激发时索引减去10s作为初始索引
start_value = data.loc[start_index]
#得到初始值
data = data.loc[intri_index:]
data = data[data>start_value]
#剔除小于初始值的数据，得到水位恢复曲线
data = data.map(lambda x:x/(-b))
#计算
data.index = [str(i) for i in range(0,len(data))]
#重置索引列
line = go.Scatter(x=data.index,y =data)
fig = go.Figure(line)
fig.show()
