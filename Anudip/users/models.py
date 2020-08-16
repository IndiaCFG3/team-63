# https://github.com/IndiaCFG3/team-63

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Application_User(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	choices = [
	
		('Manager', 'Manager'),
		('Mobilizer',  'Mobilizer')
	
	]

	type_of_user = models.CharField(max_length=9,choices = choices, default='Mobilizer')

	def __str__(self):
		return f'{self.user.username} Application User'

class Manager_to_Mob(models.Model):

	manager = models.ForeignKey(User, on_delete=models.CASCADE)

	all_mobilizers = models.ManyToManyField(User, blank=True, related_name = "+")

	def __str__(self):
		return f'{self.manager.username} Mapping'