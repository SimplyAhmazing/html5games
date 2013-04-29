from django.db import models

# Create your models here.

class Country(models.Model):
	id = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length= 30)

	def __str__(self):
		return "%s" % self.name

	def __unicode__(self):
		return "%s" % self.name

