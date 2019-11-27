from matplotlib import pyplot as plt

'''
饼图阴影、分裂等属性设置：

labels参数设置每一块的标签；
labeldistance参数设置标签距离圆心的距离（比例值）
autopct参数设置比例值小数保留位(%.3f%%)；
pctdistance参数设置比例值文字距离圆心的距离
explode参数设置每一块顶点距圆心的长度（比例值,列表）；
colors参数设置每一块的颜色（列表）；
shadow参数为布尔值，设置是否绘制阴影
startangle参数设置饼图起始角度
'''

data_li = [2,3,4,1]

plt.figure(figsize=(12,8),dpi=60)

plt.pie(
    data_li, # 用于计算比例值的数据列表，饼图根据每个值和所有值的和的百分比来绘制
    labels=['a','b','c','d'], # 每个值对于的百分比的名字，和值一一对应
    explode=[0.2,0.3,0.2,0.3], # 每个饼离圆心的距离
    labeldistance=0.5, # 标签离圆心的距离
    shadow=True, # 是不是绘制阴影
    autopct="%.3f%%", # 显示三位小数
    pctdistance=0.7, # 设置比例值数字距离圆心的距离
    colors=['yellow','orange','purple','green'], # 设置每个饼的颜色
    startangle=30, # 设置饼图的起始角度
)

plt.show()
