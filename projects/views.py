import math

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

from .models import Project, Enhancement, Bug

class IndexView(generic.ListView):
	template_name = 'projects/index.html'
	context_object_name = 'projects'

	def get_queryset(self):
		return Project.objects.all()



"""
class DetailsView(generic.DetailView):
"""


"""
class CreateView(generic.DetailView):
"""