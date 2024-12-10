# import matplotlib.pyplot as plt
#
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.serif'] = ['Times New Roman']
# # Specificity data
# specificity_values = [0.86, 0.83, 0.79, 0.82, 0.85,  0.81]
# # Sensitivity data
# sensitivity_values = [0.99, 0.97, 0.89, 0.92,  0.97, 0.84]
#
# fig, ax = plt.subplots()
#
# # Specificity
# ax.plot(specificity_values, linestyle='--', marker='o', color='black', label='Specificity')
# # Sensitivity
# ax.plot(sensitivity_values, linestyle='--', marker='s', color='grey', label='Sensitivity')
#
# ax.set_ylim(0.5, 1)
# ax.set_yticks([i/10 + 0.5 for i in range(6)])  # 设置刻度为每0.1为一个刻度，从0.5开始
#
# ax.set_xticks([])
#
# # 添加箭头到 y 轴顶点
# arrow_x = 0
# # arrow_y = max(max(specificity_values), max(sensitivity_values))
# # ax.annotate('', xy=(arrow_x, arrow_y), xytext=(arrow_x, 0), arrowprops=dict(facecolor='black', shrink=0.05))
#
# # 去掉四周的框
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_color('grey')
# ax.spines['left'].set_linewidth(0.5)
# ax.spines['bottom'].set_color('grey')
# ax.spines['bottom'].set_linewidth(0.5)
#
#
# legend = ax.legend(frameon=False)
# plt.savefig('D:/AIM-LAB/BCC/figures in lecture/sp5.png', bbox_inches='tight', dpi=300)
# plt.show()


import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']

# specificity_values = [0.86, 0.83, 0.79, 0.82, 0.85,  0.81]
# sensitivity_values = [0.99, 0.97, 0.89, 0.92,  0.97, 0.84]
sensitivity_values = [0.99, 0.88, 0.96, 0.86,  0.8, 0.8]
experts_values = [0.9, 0.81, 0.92, 0.76, 0.84, 0.73]
experts2_values = [1, 0.88, 0.97, 0.92, 0.95, 0.89]

specificity_colors = ['#7030A0', '#0067A6', '#00ABD8', '#008972', '#F5C564', '#F2572D']
sensitivity_colors = ['#7030A0', '#0067A6', '#00ABD8', '#008972', '#F5C564', '#F2572D']
experts_colors = ['#7030A0', '#0067A6', '#00ABD8', '#008972', '#F5C564', '#F2572D']

fig, ax = plt.subplots(figsize=(12, 4))



for i in range(len(experts2_values) - 1):
    ax.plot([i, i+1], [experts2_values[i], experts2_values[i+1]], linestyle='--', color='grey')

for i in range(len(sensitivity_values) - 1):
    ax.plot([i, i+1], [sensitivity_values[i], sensitivity_values[i+1]], linestyle='--', color='black')

for i in range(len(experts_values) - 1):
    ax.plot([i, i+1], [experts_values[i], experts_values[i+1]], linestyle='--', color='green')

ax.fill_between(range(len(experts2_values)), experts2_values, color='grey', alpha=0.4)
ax.fill_between(range(len(experts_values)), experts_values, color='#99cc33', alpha=0.4)

for i in range(len(experts2_values)):
    ax.scatter(i, experts2_values[i], color=specificity_colors[i], marker='^')

for i in range(len(sensitivity_values)):
    ax.scatter(i, sensitivity_values[i], color=sensitivity_colors[i], marker='s')

for i in range(len(experts_values)):
    ax.scatter(i, experts_values[i], color=experts_colors[i], marker='o')
ax.set_ylim(0.5, 1)
ax.set_yticks([i/10 + 0.5 for i in range(6)])
ax.set_xticks([])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_color('grey')
ax.spines['bottom'].set_linewidth(0.5)

# Add legend without frame
# legend = ax.legend(['Specificity', 'Sensitivity'], frameon=False)

plt.savefig('D:/AIM-LAB/BCC/figures in lecture/sp-c6.png', bbox_inches='tight', dpi=1200)
plt.show()

