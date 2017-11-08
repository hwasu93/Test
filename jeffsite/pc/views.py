# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse

def home(request):
	str = 'Hello, Yuan!'

	return render(request, 'home.html', locals())
