from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from instapy import InstaPy


def home(request):
	return render(request,'home.html',{})

def start(request):
	insta_username = 'dump_systango'
	insta_password = 'systango123'
	session = InstaPy(username=insta_username, password=insta_password, nogui=True)
	session.login()
	session.like_by_tags(['#creativewriter'], amount=100)
	session.like_by_tags(['#actors'], amount=100)
	session.like_by_tags(['#standupcomedian'], amount=100)
	session.like_by_tags(['#painter'], amount=100)
	session.like_by_tags(['#freelancewriter'], amount=100)
	session.like_by_tags(['#freelancegraphicdesigner'], amount=100)
	session.like_by_tags(['#filmmakerslife'], amount=100)
	session.like_by_tags(['#graphicdesignerlife'], amount=100)
	session.end()
	return HttpResponseRedirect('/')
