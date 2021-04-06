import numpy as np
import matplotlib.pyplot as plt


factor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

time_bubble = [3.70784, 17.1197, 48.9384, 108.287, 203.812, 331.66, 506.66, 734.56, 1034.35, 1393.88]
time_selection = [0.998017, 4.33551, 11.4106, 22.9777, 40.9867, 65.6891, 100.821, 145.615, 201.231, 269.966]
time_insertion = [0.563747, 2.65201, 6.83548, 13.8439, 24.9453, 40.6768, 62.1049, 90.2602, 125.481, 168.906]
time_merge = [0.167017, 0.463214, 1.0291, 1.7824, 2.85924, 4.09081, 5.22914, 6.69801, 8.09643, 9.66263]

plt.plot(factor, time_bubble, label = r'$Bubble$')
plt.plot(factor, time_selection, label = r'$Selection$')
plt.plot(factor, time_insertion, label = r'$Insrertion$')
plt.plot(factor, time_merge, label = r'$Merge$')

plt.xlabel(r'size, 10^3')
plt.ylabel(r'$msec$')
plt.title(r'$Sorts$')
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('sorts.png')
plt.show()


