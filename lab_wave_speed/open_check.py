import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(10, GPIO.OUT)

while True:
    GPIO.output(10,GPIO.input(24))
