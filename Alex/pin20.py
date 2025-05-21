import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
x = 1
y = 0.1
while x <=100:
    GPIO.output(20,GPIO.HIGH)
    time.sleep(y)
    GPIO.output(20,GPIO.LOW)
    time.sleep(y)
    x = x + 1
    y = y + 0.1

