import matplotlib.pyplot as plt
import numpy as np

barlist = plt.bar(["a", "b", "c"], [1, 2, 3, 4])

barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('r')
plt.show()

