import numpy as np
import matplotlib.pyplot as plt


factor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#already sorted
time_bubble_alr = [0.0003966, 0.0010948, 0.0021382, 0.0035156, 0.0108658, 0.0129222, 0.0153268, 0.0180582, 0.0211306, 0.0245448]
time_selection_alr = [0.151849, 0.778467, 2.49556, 5.26261, 9.24021, 14.7026, 22.0991, 31.7224, 43.7357, 58.5353]
time_insertion_alr = [0.0005244, 0.0015206, 0.0030206, 0.0050194, 0.00751, 0.0144452, 0.0253458, 0.0326296, 0.0371164, 0.0454058]
time_merge_alr = [0.0391412, 0.0983278, 0.156523, 0.269521, 0.377273, 0.510279, 0.659221, 0.840731, 1.14259, 1.4856]

plt.plot(factor, time_bubble_alr, label = r'$Bubble$')
plt.plot(factor, time_selection_alr, label = r'$Selection$')
plt.plot(factor, time_insertion_alr, label = r'$Insrertion$')
plt.plot(factor, time_merge_alr, label = r'$Merge$')

plt.xlabel(r' size, 10^3')
plt.ylabel(r'$msec$')
plt.title(r'$Sorts \; with \; already \; sorted \; data$')
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('sorts_alr.png')
plt.show()


