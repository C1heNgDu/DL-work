import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

data = pd.read_csv('D:/AIM-LAB/bcc_examples.csv')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']

class1 = data.iloc[:, 4]
class2 = data.iloc[:, 5]
#
std_err1 = np.std(class1) / np.sqrt(len(class1))
std_err2 = np.std(class2) / np.sqrt(len(class2))
t_statistic, p_value = stats.ttest_ind(class1, class2)
print(std_err1, std_err2)

plt.figure(figsize=(4, 4))

# box
plt.boxplot([class1, class2], patch_artist=True, zorder=0)

# points
for i, d in enumerate([class1, class2]):
    y = np.random.normal(i + 1, 0.04, size=len(d))
    plt.scatter(y, d, alpha=0.3, color='black', linewidths=0, zorder=1)
x_pos = 1.5
y_pos = max(max(class1), max(class2))
# plt.text(x_pos, y_pos, f"p-value: {p_value:.4f}", ha='center', va='bottom')
plt.xticks([1, 2], ['BCC', 'N-BCC'])
# plt.title("Box plot with Data Points")
# plt.xlabel("Group")
plt.ylabel("Probability")
plt.savefig('D:/AIM-LAB/BCC/figures in lecture/boxpoints.png', bbox_inches='tight', dpi=1200)
plt.show()
