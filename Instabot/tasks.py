from __future__ import absolute_import
from celery import Celery
from celery import task
from instapy import InstaPy
from django.core.mail import EmailMessage


celery = Celery('tasks', broker='redis://localhost:6379/0')


import os

os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "Instabot.settings"


@celery.task
def main_task():
	insta_username = 'habitsanddesign'
	insta_password = 'American1*11'
	session = InstaPy(username=insta_username, password=insta_password, nogui=True)
	session.login()
	session.like_by_tags(['#creativewriter'], amount=100)
	session.like_by_tags(['#actors'], amount=100)
	session.like_by_tags(['#standupcomedian'], amount=100)
	session.like_by_tags(['#painter'], amount=100)
	session.like_by_tags(['#freelancewriter'], amount=100)
	session.like_by_tags(['#freelancedesigner'], amount=100)
	session.like_by_tags(['#freelancegraphicdesigner'], amount=100)
	session.like_by_tags(['#filmmakerslife'], amount=100)
	session.like_by_tags(['#graphicdesignerlife'], amount=100)
	session.end()
	with open('./logs/logFile.txt', 'r') as myfile:
		data=myfile.read()
		email = EmailMessage('InstaBot Notification', data, to=['atpstpl@yopmail.com'])
		email.send()