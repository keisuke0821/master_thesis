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
x = [2015, 2016, 2018, 2020]
y = [0.066, 0.055, 0.054, 0.051]
y_errors = [0.016, 0.009, 0.007, 0.006]  # y方向のエラー

# プロット
plt.errorbar(x, y, yerr=y_errors, fmt='o', capsize=5, label="Data with error bars")

# x軸を一年単位に設定
plt.xticks(range(min(x), max(x) + 1, 1))
plt.ylim(0.04, 0.1)

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
