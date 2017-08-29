# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index( request ):
    return render(request, "create_posts/index.html")

def add(request):
	Notes.objects.create(description=request.POST['create_form'])
	notes=Notes.objects.order_by('-id')
	return render(request,"create_posts/notes.html",{'notes': notes})