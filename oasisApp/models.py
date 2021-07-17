from django.db import models
from django.contrib.auth import User 

# Create your models here.
class Activity(models.Model):
	CATEGORY = (
		('POOL','POOL'),
		('BAR','BAR'),
		('CHILL_ROOM','CHILL_ROOM'),
		('RESTAURANT','RESTAURANT'),
		('ROOMS','ROOMS'),
		('HAMAM','HAMAM'),
		('MASSAGE_ROOM','MASSAGE_ROOM')
		)

	activity_name = models.CharField(max_length=300)
	activity_description = models.CharField(max_length=300 ,null= True)
	category = models.CharField(max_length=300, choices=CATEGORY, null=True)

	def __str__(self):
		return self.activity_name

class Client(models.Model):
	