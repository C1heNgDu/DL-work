import matplotlib.pyplot as plt
# 设置字体为新罗马
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']

categories = ['BCC', 'N-BCC']
# categories = ['arborizing vessels', 'ulceration', 'shiny white structures', 'blue-grey ovoid nests', 'blue-grey globules', 'leaf-like structures', 'spoke wheel structures']
data = [3000, 2000]
# data = [142, 138, 129, 116, 93, 76, 62]

fig, ax = plt.subplots(figsize=(12, 6))
# B4C7E7 FFE699
bars = ax.barh(categories, data, color=['#B4C7E7', '#FFE699'])
# bars = ax.barh(categories, data, color=['#0067A6', '#7030A0', '#F5C564', '#F2572D', '#00ABD8', '#43978F', '#E56F5E'])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ax.set_xlabel('AP (%)')

# 在柱子右边显示数值除以300的百分比，保留两位小数
# for bar, value in zip(bars, data):
#     percentage = round(value / 100 * 100, 2)
#     ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2, f'{percentage}%', ha='left', va='center', color='black', fontweight='bold')

plt.savefig('D:/AIM-LAB/BCC/figures in lecture/data_bar_chart-S1.png', bbox_inches='tight', dpi=1200)
plt.show()
