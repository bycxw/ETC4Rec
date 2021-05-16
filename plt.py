# coding: utf-8
# @Time:    2021/4/8 1:28
# @Author:  bycxw

"""
plot
"""

import matplotlib.pyplot as plt

def plot_gsl():
    x_axis = range(6)
    HR_1 = [0.1969, 0.2140, 0.2064, 0.2063, 0.2050, 0.2013]
    HR_5 = [0.4514, 0.4650, 0.4610, 0.4564, 0.4629, 0.4582]
    HR_10 = [0.5811, 0.5957, 0.5973, 0.5913, 0.5935, 0.5901]
    NDCG_5 = [0.3284, 0.3443, 0.3383, 0.3367, 0.3383, 0.3347]
    NDCG_10 = [0.3704,  0.3864, 0.3823, 0.3801, 0.3804, 0.3771]
    MRR = [0.3223, 0.3383, 0.3322, 0.3316, 0.3309, 0.3280]

    plt.plot(x_axis, HR_1, color="r", marker="^", linewidth=1)
    plt.plot(x_axis, HR_5, color="b", marker="s", linewidth=1)
    plt.plot(x_axis, HR_10, color="g", marker="o", linewidth=1)
    plt.plot(x_axis, NDCG_5, color="c", marker="v", linewidth=1)
    plt.plot(x_axis, NDCG_10, color="m", marker="<", linewidth=1)
    plt.plot(x_axis, MRR, color="y", marker=">", linewidth=1)

    plt.legend(["HR@1", "HR@5", "HR@10", "NDCG@5", "NDCG@10", "MRR"],loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)

    plt.ylim(0.1, 0.7)

    plt.xticks(x_axis, [1, 2, 4, 8, 16, 32])

    plt.xlabel("Global Input Length")
    plt.ylabel("Performance")

    plt.show()

def plot_lr():
    x_axis = range(5)
    HR_1 = [0.2303, 0.2400, 0.2302, 0.2154, 0.2050]
    HR_5 = [0.4840, 0.5017, 0.4903, 0.4677, 0.4629]
    HR_10 = [0.6112, 0.6216, 0.6185, 0.6018, 0.5935]
    NDCG_5 = [0.3623, 0.3763, 0.3657, 0.3461, 0.3383]
    NDCG_10 = [0.4032, 0.4152, 0.4071, 0.3894, 0.3804]
    MRR = [0.3546, 0.3666, 0.3571, 0.3401, 0.3309]

    plt.plot(x_axis, HR_1, color="r", marker="^", linewidth=1)
    plt.plot(x_axis, HR_5, color="b", marker="s", linewidth=1)
    plt.plot(x_axis, HR_10, color="g", marker="o", linewidth=1)
    plt.plot(x_axis, NDCG_5, color="c", marker="v", linewidth=1)
    plt.plot(x_axis, NDCG_10, color="m", marker="<", linewidth=1)
    plt.plot(x_axis, MRR, color="y", marker=">", linewidth=1)

    plt.legend(["HR@1", "HR@5", "HR@10", "NDCG@5", "NDCG@10", "MRR"],loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)

    plt.ylim(0.1, 0.7)

    plt.xticks(x_axis, [2, 4, 8, 16, 32])
    plt.xlabel("local radius")
    plt.ylabel("performance")

    plt.show()


if __name__ == "__main__":
    plot_gsl()
    # plot_lr()
