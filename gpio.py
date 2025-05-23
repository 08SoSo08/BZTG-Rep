import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)

while True:
    	GPIO.output(16,GPIO.HIGH)