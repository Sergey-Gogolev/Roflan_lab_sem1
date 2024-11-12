import matplotlib.pyplot as plt
import numpy as np


depth = np.array([])
volts = np.array([])
with open('kolibrovka.txt','r') as file:
    for line in file.readlines():
        depth = np.append(depth, float(line.split()[0]))
        volts = np.append(volts, float(line.split()[1]))

plt.plot(depth, volts)
plt.show()