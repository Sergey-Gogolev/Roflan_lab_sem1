from matplotlib import pyplot as plt
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D

def atm(v2):
    r=8.31446
    t=298.15

    x_noa=0.99964
    m_noa=0.02897
    c_p_noa=1.0036
    c_v_noa=0.7166

    m_y=0.04401
    c_p_y=0.838
    c_v_y=0.649

    m_h=0.01801
    c_p_h=1.863
    c_v_h=1.403
    n=1-(0.3*3170)/(101375)
    k1=n*m_y*c_p_y
    k2=n*m_y*c_v_y
    k3=n*m_y
    a=x_noa*n*m_noa*c_p_noa + (1-n)*m_h*c_p_h
    b=x_noa*n*m_noa*c_v_noa + (1-n)*m_h*c_v_h
    c=x_noa*n*m_noa + (1-n)*m_h

    e1=v2*k2*k3
    e2=v2*(k2*c+k3*b)-k1*r*t
    e3=v2*b*c-a*r*t

    d = e2 ** 2 - 4 * e1 * e3
    x = (-e2 + d ** 0.5) / (2 * e1)
    if x>-0.0002 and x<=0.001:
        print(x)
        print(v2**0.5)
    return x


def langs(v2):
    r=8.31446
    t=295.15

    x_noa=0.99964
    m_noa=0.02897
    c_p_noa=1.0036
    c_v_noa=0.7166

    m_y=0.04401
    c_p_y=0.838
    c_v_y=0.649

    m_h=0.01801
    c_p_h=1.863
    c_v_h=1.403
    n=1-(1*3170)/(101375)
    k1=n*(m_y-m_noa)*c_p_y
    k2=n*(m_y-m_noa)*c_v_y
    k3=n*(m_y-m_noa)
    a=x_noa*n*m_noa*c_p_noa + (1-n)*m_h*c_p_h
    b=x_noa*n*m_noa*c_v_noa + (1-n)*m_h*c_v_h
    c=x_noa*n*m_noa + (1-n)*m_h
    e1=v2*k2*k3
    e2=v2*(k2*c+k3*b)-k1*r*t
    e3=v2*b*c-a*r*t
    d = e2 ** 2 - 4 * e1 * e3
    x = (-e2 + d ** 0.5) / (2 * e1)
    if x>=0.035 and x<=0.045:
        print(x)
        print(v2**0.5)
    return x

mas_conc_atm =[]
mas_v_atm = []
for i in range(3410 , 3469):
    mas_v_atm.append(i/10)
for i in mas_v_atm:
    mas_conc_atm.append(atm(i**2)*100)
mas_conc_langs =[]
mas_v_langs = []
for i in range(3410, 3469):
    mas_v_langs.append(i/10)
for i in mas_v_langs:
    mas_conc_langs.append(langs(i**2)*100)
plt.plot(mas_conc_atm, mas_v_atm, color = 'g', label = "атмосферный воздух")
plt.plot(mas_conc_langs, mas_v_сs, color = 'b', label = "выдыхаемый воздух")
plt.legend()
plt.scatter(0.18 , 346.29)
plt.scatter(1.25, 345.05)
plt.title("Зависимость скорости звука от содержания углекислого газа")
plt.xlabel("содержание углекислого газа, %")
plt.ylabel("скорость звукаб м/с")
plt.grid(True)
plt.show()
