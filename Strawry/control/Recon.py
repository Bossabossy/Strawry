import time
import os
import sys
import RPi.GPIO as GPIO

# class Recon(object):
	
# 	GPIO.setmode(GPIO.BOARD)

	


# 	# relay for light 1
# 	L_PIN = 9 
# 	def GPIOsetup():
# 		GPIO.setmode(GPIO.BCM)
# 		GPIO.setup(L_PIN, GPIO.OUT)
# 		GPIO.setwarnings(False)

	
# 	def lon():
# 		


# 	def l1off():
# 		GPIO.output(L_PIN, 1)
# 		print "light off"
# 		return()


	


# 	# relay for PUMP
# 	PUMP_PIN = 10 
# 	def GPIOsetup():
# 	GPIO.setmode(GPIO.BCM)
# 	GPIO.setup(PUMP_PIN, GPIO.OUT)
# 	GPIO.setwarnings(False)

# 	def pumpon():
# 	GPIO.output(PUMP_PIN, 0)
# 	print "light on"
# 	return()

# 	def pumpoff():
# 	GPIO.output(PUMP_PIN, 1)
# 	print "light off"
# 	return()
	


# 	# relay for humidity
# 	HUMI_PIN = 11 
# 	def GPIOsetup():
# 	GPIO.setmode(GPIO.BCM)
# 	GPIO.setup(HUMI_PIN, GPIO.OUT)
# 	GPIO.setwarnings(False)

# 	def humion():
# 	GPIO.output(HUMI_PIN, 0)
# 	print "light on"
# 	return()

# 	def humioff():
# 	GPIO.output(HUMI_PIN, 1)
# 	print "light off"
# 	return()

	


# 	# relay for compressor
# 	COM_PIN = 12 
# 	def GPIOsetup():
# 	GPIO.setmode(GPIO.BCM)
# 	GPIO.setup(COM_PIN, GPIO.OUT)
# 	GPIO.setwarnings(False)

# 	def comon():
# 	GPIO.output(COM_PIN, 0)
# 	print "light on"
# 	return()

# 	def comoffs():
# 	GPIO.output(COM_PIN, 1)
# 	print "light off"
# 	return()


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






