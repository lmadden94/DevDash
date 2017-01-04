from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
	task_name = models.CharField(max_length=200)
	task_description = models.TextField(max_length=500, blank=True, null=True)
	creator = models.ForeignKey(User, related_name='task_creator')
	executor = models.ForeignKey(User, related_name='task_executor')
	completed = models.BooleanField(default=False)
	completed_on = models.DateTimeField('date completed', blank=True, null=True)
	date_started = models.DateTimeField('date started')

	def __str__(self):
		return self.task_name