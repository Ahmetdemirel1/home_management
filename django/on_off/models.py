from django.db import models

# Create your models here.
class Device(models.Model):
	name = models.CharField(max_length=200)
	on = models.BooleanField()
	signal_on = models.CharField(max_length=1)
	signal_off = models.CharField(max_length=1)
	def __unicode__(self):
		return self.name

class Sensor(models.Model):
	name = models.CharField(max_length=200)
	signal = models.CharField(max_length=1)
	def __unicode__(self):
		return self.name
