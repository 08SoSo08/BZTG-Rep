import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
#GPIO.setup(16,GPIO.OUT)
GPIO.setup(5,GPIO.IN)
""" x = 1
y = 0.1
while x <=100:
    GPIO.output(20,GPIO.HIGH)
    time.sleep(y)
    GPIO.output(20,GPIO.LOW)
    time.sleep(y)
    x = x + 1
    y = y + 0.1 """
while True:
    if GPIO.input(5)==0:
        GPIO.output(20,GPIO.LOW)
    else:
        GPIO.output(20,GPIO.HIGH)


