import math

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

from .models import Task

class IndexView(generic.ListView):
	template_name = 'tasks/index.html'
	context_object_name = 'tasks'

	def get_queryset(self):
		return Task.objects.filter(completed=False).all()