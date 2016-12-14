from django.shortcuts import render
from login.form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
# Create your views here.


def frontpage(request):
    return render(request, 'cover/cover_page.html', {})
