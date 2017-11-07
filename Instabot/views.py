from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from tasks import main_task


def home(request):
	return render(request,'home.html',{})

def start(request):
	main_task.delay()
	return HttpResponseRedirect('/')
