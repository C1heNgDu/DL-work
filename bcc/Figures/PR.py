import matplotlib.pyplot as plt

# A类的Precision和Recall
precision_a = [0.561, 0.906, 0.426, 0.501, 0.615]
recall_a = [0.486, 0.614, 0.614, 0.533, 0.675]

# B类的Precision和Recall
precision_b = [0.129, 0.165, 0.200, 0.505 , 0.236]
recall_b = [0.225, 0.225, 0.200,  0.225, 0.233]

# 绘制PR曲线
plt.plot(recall_a, precision_a, label='Class A')
plt.plot(recall_b, precision_b, label='Class B')

# 添加标签
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()

# 显示图形
plt.show()
