import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

pin=7
GPIO.output(pin, 1)
time.sleep(1)
GPIO.output(pin, 0)
time.sleep(1)
GPIO.output(pin, 1)

pin=8
GPIO.output(pin, 1)
time.sleep(1)
GPIO.output(pin, 0)
time.sleep(1)
GPIO.output(pin, 1)

pin=9
GPIO.output(pin, 1)
time.sleep(1)
GPIO.output(pin, 0)
time.sleep(1)
GPIO.output(pin, 1)

pin=10
GPIO.output(pin, 1)
time.sleep(1)
GPIO.output(pin, 0)
time.sleep(1)
GPIO.output(pin, 1)

pin=11
GPIO.output(pin, 1)
time.sleep(1)
GPIO.output(pin, 0)
time.sleep(1)
GPIO.output(pin, 1)

time.sleep(5)
GPIO.cleanup()
