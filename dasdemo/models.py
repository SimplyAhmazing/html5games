from django.db import models

#from typeahead.models import Country
# Create your models here.



class Country(models.Model):
	short = models.CharField(max_length=5)
	name = models.CharField(max_length= 30)

	def __str__(self):
		return "%s" % self.name

	def __unicode__(self):
		return "%s" % self.name

class Cars(models.Model):
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	country = models.ForeignKey(Country, blank=True, null=True)

	def __str__(self):
		return "%s" % self.name

	def __unicode__(self):
		return "%s" % self.name