from __future__ import unicode_literals
from django.db import models



class Table(models.Model):
	time=models.DateTimeField(auto_now_add=True)
	temp=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
	humi=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)	
	CO2=models.FloatField()
	light=models.BooleanField(default=True)
	watp=models.BooleanField(default=True)
	
	def __str__(self):
		return "{} {} {} {} {} {}".format(self.time, self.temp, self.humi, self.CO2, self.light, self.watp)
		