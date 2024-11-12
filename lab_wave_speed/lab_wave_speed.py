import matplotlib.pyplot as plt
import numpy as np

def mnk_k(x,y):                                                                         # МНК
    k = (np.mean(x*y) - np.mean(x)*np.mean(y)) / (np.mean(x**2) - np.mean(x)**2)
    return k

def mnk_b(x,y):
    b = np.mean(y) - mnk_k(x,y)*np.mean(x)
    return b

h = []
u = []

with open("C:/Users/gogol/Desktop/labs/RPILabs/lab_wave_speed/laba/kolibrovka.txt",'r') as file:                                    # Глубина от напряжения
    for line in file.readlines():
        h.append(float(line.split()[0]))
        u.append(float(line.split()[1])/50)                                # В файле записаны значения напряжения как сумма 50 точек
k = np.polyfit(u, h, 2)
def height_measure(u_val):
    return np.polyval(k, u_val)

depths = ['45','70','82','100','110']
v = []
plt.figure(figsize=(6,8), dpi=100)
for depth in depths:
    h = []
    t = []
    with open(f"C:/Users/gogol/Desktop/labs/RPILabs/lab_wave_speed/laba/data{depth}.0.txt",'r') as file:
        for line in file.readlines():
            t.append(float(line.split()[0]))
            h.append(height_measure(float(line.split()[1])))

    for i in range(2, len(t)):                                                     # Ждем, пока модуль производная в окрестности какого-то значения времени меньше опр. значения
        T = np.array(t[i - 4:i + 5])
        H = np.array(h[i - 4:i + 5])
        if (abs(mnk_k(T,H)) > 13.0):
            v.append(1.2 / t[i])
            break


    plt.plot(t,h,label=f'{depth} mm')
#############
plt.legend()
plt.minorticks_on()
plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1.5,
         color='0.7')
plt.grid(visible=True,
         which='minor',
         linestyle='--',
         linewidth=1,
         color='0.8')
plt.xlabel(r"Время, c")
plt.ylabel(r"Глубина, мм")
plt.savefig("pic1.png")
########
for i in range(len(depths)):
    print("h = {}   v = {}   v_teor = {}".format(float(depths[i]), v[i], np.sqrt(float(depths[i])/1000 * 9.82)))

plt.figure(figsize=(6,8), dpi=100)

log_depth = np.array([np.log(float(x)/1000) for x in depths])                   # Последний пункт лабы
log_v = np.array([np.log(x) for x in v])

plt.errorbar(log_depth, log_v, lw=0,
             capsize=0,
             c = 'red',
             marker = 'o',
             ms = 4,label='result')
x = np.linspace(min(log_depth), max(log_depth),5)
plt.plot(x, x * mnk_k(log_depth,log_v) + mnk_b(log_depth,log_v),label='approximation')
######
plt.legend()
plt.minorticks_on()
plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1.5,
         color='0.7')
plt.grid(visible=True,
         which='minor',
         linestyle='--',
         linewidth=1,
         color='0.8')
plt.xlabel(r"ln(Глубина)")
plt.ylabel(r"ln(Скорость)")

plt.savefig("pic2.png")
#########
print(mnk_k(log_depth,log_v), mnk_b(log_depth,log_v))

plt.show()

