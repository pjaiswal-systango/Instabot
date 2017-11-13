from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from tasks import main_task


def home(request):
	return render(request,'home.html',context={'is_started': False})

def start(request):
	main_task.delay()
	return render(request,'home.html',context={'is_started': True})
