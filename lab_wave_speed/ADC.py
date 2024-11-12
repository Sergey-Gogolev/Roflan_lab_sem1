import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
levels = 256
maxVolts = 3.09

def decimal_to_binary(x):
    return [int(n) for n in bin(x)[2:].zfill(8)]

def binary_to_decimal(a):
    return int(''.join(a), 2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(10, GPIO.OUT)

try:
    lk = float(input())
    while(not GPIO.input(24)):
        pass
    deep = np.array([0. for i in range(1000)])
    volts = 0
    time_start = time.time()
    ra = range(8)
    j = 0
    base = np.array([0,0,0,0,0,0,0,0])
    while(True):
        signal = base.copy()
        for i in ra:
            signal[i] = 1
            GPIO.output(dac, signal)
            time.sleep(0.003)
            signal[i] = GPIO.input(comp) > 0
        #val = binary_to_decimal(signal)
       # volts = val/levels * 3.09
        #print("ADC val = {:^3} -> {}, input voltage = {:.2f}".format(val, signal, volts))
        deep[j] = binary_to_decimal(signal)
        j+=1
    for i in range(j-1):
        deep[i]*= 3.09/levels

#   time_end = time.time()
 #   with open('kolibrovka.txt','a') as f:
  #      f.write(deep+'\t'+str(volts+'\n')

except KeyboardInterrupt:
    time_end=time.time()
    t = np.linspace(0, time_end - time_start, len(deep))
    plt.plot(t, deep)
    with open('data{}.txt'.format(lk), 'w') as f:
        for i in range(len(t)):
            f.write('{} {}\n'.format(t[i], deep[i]))
    plt.show()
    print('Program was stopped by User')
else:
    print('No exceptions')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    print()
    print('VSE')
    print()