from Recon import Recon , SensorReader
import time
control = Recon()
read = SensorReader()

control.com_on()
time.sleep(1)
control.light_on()
time.sleep(1)
control.ex_on()
time.sleep(1)
control.humi_on()
time.sleep(1)
control.pump_on()
time.sleep(1)

time.sleep(0)
control.com_off()
time.sleep(1)
control.light_off()
time.sleep(1)
control.ex_off()
time.sleep(1)
control.humi_off()
time.sleep(1)
control.pump_off()
time.sleep(1)
control.clean()

#import RPi.GPIO as GPIO
#pin=11
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(pin,GPIO.OUT)
#GPIO.output(pin, 1)
#time.sleep(1)
#GPIO.output(pin, 0)
#time.sleep(1)
#GPIO.output(pin, 1)
#time.sleep(5)
#GPIO.cleanup()
