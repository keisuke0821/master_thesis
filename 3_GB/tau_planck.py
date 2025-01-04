import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#%matplotlib inline
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (8,6)
plt.rcParams['figure.edgecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True

# データ
x = [2003,2013, 2015, 2018, 2020, 2023]
y = [0.117, 0.081, 0.066, 0.056, 0.051, 0.058]
y_errors = [0.055, 0.012, 0.012, 0.007, 0.006, 0.006]  # y方向のエラー

x_arange = [1, 5, 7, 10, 12, 15]

# プロット
plt.errorbar(x_arange, y, yerr=y_errors, fmt='o', capsize=5, label="Data with error bars")

# x軸を一年単位に設定
#plt.xticks(range(min(x), max(x) + 1, 1))
plt.xticks(x_arange, x)
#plt.ylim(0.04, 0.1)

# ラベルとタイトル
plt.xlabel("Year")
plt.ylabel(r"Optical depth $\tau$ ")
#plt.title("Plot with Y Error Bars")

# グリッドと凡例
plt.grid(True)
plt.tight_layout()
#plt.legend()

# グラフを表示
plt.show()
