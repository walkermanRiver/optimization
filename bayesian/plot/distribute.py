import numpy as np
import matplotlib.pyplot as plt


def plot_distribution(data):
    # 设置图片清晰度
    plt.rcParams['figure.dpi'] = 300

    # 绘制直方图
    plt.hist(data, bins=30, edgecolor='black')

    # 添加图标题和坐标轴标签
    plt.title('Distribution of Values')
    plt.xlabel('Value')
    plt.xticks(rotation=45)
    plt.ylabel('Frequency')

    # 显示图形
    plt.show()


if __name__ == "__main__":
    # 生成一个示例数组
    sample_array = np.random.normal(loc=0, scale=1, size=1000)

    # 调用函数绘制分布图
    plot_distribution(sample_array)