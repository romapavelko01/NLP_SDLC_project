# import numpy as np
import matplotlib.pyplot as plt
# import scipy.stats as stats
# import math
#
# MEAN = 5
# scales = [1, 2, 4, 5]
# colors = ['r', 'b', 'g']
# plt.figure(figsize=(15, 5))
# for scale, color in zip(scales, colors):
#     x = np.linspace(MEAN - 3*scale, MEAN + 3*scale, 100)
#     plt.plot(x, stats.norm.pdf(x, MEAN, scale), color=color, label=f"scale={scale}")
#
# plt.legend()
# plt.show()
fig = plt.figure(3, figsize=(15, 5), dpi=300)
ax = fig.add_subplot(2, 2, 1)
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
plt.show()