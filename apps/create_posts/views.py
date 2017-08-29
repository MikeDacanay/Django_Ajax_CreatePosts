# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index( request ):
    return render(request, "create_posts/index.html")

def add(request):
	print request.POST['create_form']
	return redirect('/')