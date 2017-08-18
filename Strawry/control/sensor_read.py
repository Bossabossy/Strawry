
import sys

import Adafruit_DHT

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
