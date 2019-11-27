from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="msyhbd.ttc")

a = []

# 设置统计数据的间隔，从而计算总共有多少个间隔
distance = 3
num_bins = (max(a)-min(a))//distance + 1

plt.figure(figsize=(12,5),dpi=80)

# 绘制直方图，用来查看数据在某段中的分布情况
plt.hist(a,num_bins)

# 设置x轴显示的内容
plt.xticks(range(min(a),max(a)+distance,distance))

plt.grid()

plt.show()