import time
import os
import sys
import RPi.GPIO as GPIO

class Recon(object):
	GPIO.setmode(GPIO.BOARD)

	# relay for light 1
	L1_PIN = 9 
	def GPIOsetup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(L1_PIN, GPIO.OUT)
	GPIO.setwarnings(False)

	def L1ON():
	GPIO.output(L1_PIN, 0)
	print "light on"
	return()

	def L1OFF():
	GPIO.output(L1_PIN, 1)
	print "light off"
	return()

	#relay for light 2
	L2_PIN = 10 
	def GPIOsetup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(L2_PIN, GPIO.OUT)
	GPIO.setwarnings(False)

	def L2ON():
	GPIO.output(L2_PIN, 0)
	print "light on"
	return()

	def L2OFF():
	GPIO.output(L2_PIN, 1)
	print "light off"
	return()

	# relay for PUMP
	PUMP_PIN = 11 
	def GPIOsetup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PUMP_PIN, GPIO.OUT)
	GPIO.setwarnings(False)

	def PUMPON():
	GPIO.output(PUMP_PIN, 0)
	print "light on"
	return()

	def PUMPOFF():
	GPIO.output(PUMP_PIN, 1)
	print "light off"
	return()
	# relay for humidity
	HUMI_PIN = 12 
	def GPIOsetup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(HUMI_PIN, GPIO.OUT)
	GPIO.setwarnings(False)

	def HUMION():
	GPIO.output(HUMI_PIN, 0)
	print "light on"
	return()

	def HUMIOFF():
	GPIO.output(HUMI_PIN, 1)
	print "light off"
	return()

	# relay for compressor
	COM_PIN = 13 
	def GPIOsetup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(COM_PIN, GPIO.OUT)
	GPIO.setwarnings(False)

	def COMON():
	GPIO.output(COM_PIN, 0)
	print "light on"
	return()

	def COMOFF():
	GPIO.output(COM_PIN, 1)
	print "light off"
	return()


