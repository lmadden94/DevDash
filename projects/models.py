from django.db import models

# Create your models here.


class Project(models.Model):
	project_name = models.CharField(max_length=200)
	date_started = models.DateTimeField('date started')

	def __str__(self):
		return self.project_name

	def bug_count(self):
		return self.bug_set.filter(completed=False).count()

	def enhancement_count(self):
		return self.enhancement_set.filter(completed=False).count()

	def possible_colors(self):
		return {'red', 'orange', 'yellow', 'green', 'teal', 'blue', 'violet', 'purple'}


class Enhancement(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	enhancement_title = models.CharField(max_length=100)
	enhancement_description = models.TextField(max_length=500)
	completed = models.BooleanField(default=False)
	completed_on = models.DateTimeField('date completed')

	def __str__(self):
		return self.enhancement_title


class Bug(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	bug_title = models.CharField(max_length=100)
	bug_description = models.TextField(max_length=500)
	completed = models.BooleanField(default=False)
	completed_on = models.DateTimeField('date completed')

	def __str__(self):
		return self.bug_title