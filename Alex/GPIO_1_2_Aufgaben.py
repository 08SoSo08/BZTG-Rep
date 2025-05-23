import RPi.GPIO as GPIO
import time
import dht11



GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(26,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(22,GPIO.OUT)
data = dht11.DHT11(pin=18)


while True:
    #if GPIO.input(26) == 1:
          #GPIO.output(16,GPIO.HIGH)
          #GPIO.output(6,GPIO.HIGH)
    #else:
        #GPIO.output(16,GPIO.LOW) 
        #GPIO.output(6,GPIO.LOW)
    while GPIO.input(19) == 1:
            GPIO.output(20,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(20,GPIO.LOW)
            time.sleep(0.5)
    while GPIO.input(13) == 1:
            GPIO.output(21,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(21,GPIO.LOW)
            time.sleep(0.5)
    indoor = data.read()
    if indoor.is_valid():   
          print ("temperatur:" + str(indoor.temperature)) 
          print("Luftfeuchtigkeit:" + str(indoor.humidity))
          x = indoor.temperature
          if x >= 25.0:
              GPIO.output(22,GPIO.HIGH)
          else:
              GPIO.output(22,GPIO.LOW)
GPIO.cleanup()





