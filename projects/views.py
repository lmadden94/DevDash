import math

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'projects/index.html'
	context_object_name = 'all_projects'



"""
class DetailsView(generic.DetailView):
"""


"""
class CreateView(generic.DetailView):
"""