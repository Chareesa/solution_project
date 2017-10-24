# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User

# Create your views here.
def home(request):
	if 'first_name' not in request.session:
		return redirect('/')
	context = {
		'other_users': User.objects.exclude(id = request.session['id'])
	}
	return render(request, 'main_app/index.html', context)