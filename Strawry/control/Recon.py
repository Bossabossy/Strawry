import time
import os
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
from datetime import datetime
# output data section
class Recon(object):
	def __init__(self, light_pin=8 ,pump_pin = 11, humi_pin = 10 , com_pin=7 ,ex_pin=9):
		self.light_pin = light_pin
		self.humi_pin = humi_pin
		self.pump_pin = pump_pin
		self.com_pin = com_pin
		self.ex_pin = ex_pin
		self.last_com=datetime.now()
		self.last_light=datetime.now()
		self.last_pump=datetime.now()
		self.last_humi=datetime.now()
		self.last_ex=datetime.now()

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.light_pin,GPIO.OUT)
		GPIO.setup(self.humi_pin,GPIO.OUT)
		GPIO.setup(self.pump_pin,GPIO.OUT)
		GPIO.setup(self.com_pin,GPIO.OUT)
		GPIO.setup(self.ex_pin,GPIO.OUT)
		GPIO.output(self.light_pin, 0)
		GPIO.output(self.humi_pin, 0)
		GPIO.output(self.com_pin, 0)
		GPIO.output(self.ex_pin, 0)
		GPIO.output(self.pump_pin, 0)
	def light_on(self):
		if (datetime.now()-self.last_light).seconds>5:		
			GPIO.output(self.light_pin, 1)
			print ("light on")
			self.last_light=datetime.now()


	def light_off(self):
		if (datetime.now()-self.last_light).seconds>5:
			GPIO.output(self.light_pin, 0)
			print ("light off")
			self.last_light=datetime.now()


	def humi_on(self):
		if (datetime.now()-self.last_humi).seconds>60:
			GPIO.output(self.humi_pin, 1)
			print ("humi on")
			self.last_humi=datetime.now()
			

	def humi_off(self):
		if (datetime.now()-self.last_humi).seconds>60:
			GPIO.output(self.humi_pin, 0)
			print ("humi off")
			self.last_humi=datetime.now()

	def pump_on(self):
		if (datetime.now()-self.last_humi).seconds>10:
			GPIO.output(self.pump_pin, 1)
			print ("pump on")
			self.last_humi=datetime.now()
		

	def pump_off(self):
		if (datetime.now()-self.last_pump).seconds>10:
			GPIO.output(self.pump_pin, 0)
			print ("pump off")
			self.last_pump=datetime.now()

	def com_on(self):
		if (datetime.now()-self.last_com).seconds>60:
			GPIO.output(self.com_pin, 1)
			print ("com on")
			self.last_com=datetime.now()

	def com_off(self):
		if (datetime.now()-self.last_com).seconds>60:
			GPIO.output(self.com_pin, 0)
			print ("com off")
			self.last_com=datetime.now()
	def ex_on(self):
		if (datetime.now()-self.last_ex).seconds>60:		
			GPIO.output(self.ex_pin, 1)
			print ("ex on")
			self.last_ex=datetime.now()

	def ex_off(self):
		if (datetime.now()-self.last_ex).seconds>60:
			GPIO.output(self.ex_pin, 0)
			print ("ex off")
			self.last_ex=datetime.now()
	def clean(self):
		GPIO.cleanup()



# import sys

# import Adafruit_DHT

# Input data section
class SensorReader(object):
	def __init__(self, sensor = 22 , pin = 4 ):
		self.sensor = sensor
		self.pin = pin

	def read_DHT(self):
		return Adafruit_DHT.read_retry(self.sensor,self.pin)

	def get_temp(self):
		return Adafruit_DHT.read_retry(self.sensor,self.pin)[1]

	def get_humi(self):
		return Adafruit_DHT.read_retry(self.sensor,self.pin)[0]




