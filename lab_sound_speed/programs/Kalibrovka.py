import numpy as np
import matplotlib.pyplot as plt
x = np.genfromtxt("vdox1.txt", delimiter='\n')
y = np.linspace(1,4999,4999)
x1 = np.genfromtxt("vdox2.txt", delimiter='\n')
plt.plot((y+1680), (x-430), y[:-1], x1)
plt.ylabel("Показания АЦП")
plt.xlabel("Номер отсчета")
plt.grid(True)
plt.show()
