from django.db import models
from django.contrib.auth.models import User 

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
	name = models.CharField(max_length=300)
	email = models.CharField(max_length= 300, null=True)
	date_registered = models.DateTimeField(auto_now_add=True , null= True)

	def __str__(self):
		return self.name


class Client_Database(models.Model):
	date_registered = models.DateTimeField(auto_now_add=True , null= True)
	client = models.ForeignKey(User, null=True , on_delete=models.SET_NULL)
	activities = models.ForeignKey(Activity,null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.activities


class Staff_Database_Access(models.Model):
	date_registered = models.DateTimeField(auto_now_add=True , null= True)
	client = models.ForeignKey(Client, null=True , on_delete=models.SET_NULL)
	activities = models.ForeignKey(Activity,null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return f'Client {self.client}:Activity {self.activities}:Booked at {sefl.date_registered}'






