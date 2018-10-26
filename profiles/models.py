from django.db import models

# Create your models here.

class profile(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=120,default='This is my app')
	location = models.CharField(max_length=120, blank=True)
	job = models.CharField(max_length=120, blank=True)

	def __unicode__(self):
		return self.name
