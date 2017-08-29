#from Recon import Recon
import time
#control = Recon()


#control.humi_off()
#control.pump_off()
#control.humi_off()
#control.com_off()
#time.sleep(10)
#control.com_on()
#time.sleep(10)
#control.clean()
time.sleep(20)
import RPi.GPIO as GPIO
pin=11
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin, 1)
time.sleep(1)
GPIO.output(pin, 0)
time.sleep(1)
GPIO.output(pin, 1)
time.sleep(5)
GPIO.cleanup()
