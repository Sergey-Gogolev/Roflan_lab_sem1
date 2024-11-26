import matplotlib.pyplot as plt
import numpy as np
a = []
b = []
with open('/home/b03-404/Downloads/room_0.txt') as f:
    a = np.array(list(map(float, f.read().split()))[:-1])
with open('/home/b03-404/Downloads/room_1.txt') as f:
    b = np.array(list(map(float, f.read().split())))
n = len(b)

t = np.linspace(0, n-1, n) 
a -= a[1]
b -= b[1]
plt.plot(t+1672, a/387)
plt.plot(t, b/162)
plt.show()