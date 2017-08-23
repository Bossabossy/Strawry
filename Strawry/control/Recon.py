import time
import os
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
# output data section
class Recon(object):
	def __init__(self, light_pin=9 ,pump_pin = 10, humi_pin = 11 , com_pin= 8):
		self.light_pin = light_pin
		self.humi_pin = humi_pin
		self.pump_pin = pump_pin
		self.com_pin = com_pin
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.light_pin,GPIO.OUT)
		GPIO.setup(self.humi_pin,GPIO.OUT)
		GPIO.setup(self.pump_pin,GPIO.OUT)
		GPIO.setup(self.com_pin,GPIO.OUT)


	def light_on(self):
		
		GPIO.output(self.light_pin, 1)
		print ("light on")
		

	def light_off(self):
		
		GPIO.output(self.light_pin, 0)
		print ("light off")
		

	def humi_on(self):
		
		GPIO.output(self.humi_pin, 1)
		print ("humi on")
		

	def humi_off(self):
		
		GPIO.output(self.humi_pin, 0)
		print ("humi off")

	def pump_on(self):
		
		GPIO.output(self.pump_pin, 1)
		print ("pump on")
		

	def pump_off(self):
		
		GPIO.output(self.pump_pin, 0)
		print ("pump off")

	def com_on(self):
		
		GPIO.output(self.com_pin, 1)
		print ("com on")
		

	def com_off(self):
		
		GPIO.output(self.com_pin, 0)
		print ("com off")

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




