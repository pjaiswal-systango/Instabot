from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from tasks import main_task


def home(request):
	is_started = False
	if 'is_started' in request.session:
		if request.session['is_started'] == True:
			is_started = True
			request.session['is_started'] = False
	return render(request,'home.html', context={'is_started': is_started})

def start(request):
	request.session['is_started'] = True
	main_task.delay()
	return HttpResponseRedirect(reverse('home'))
