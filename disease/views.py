from django.http import HttpResponse
from models import Disease
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import Http404


def index(request):
	d = Disease.objects.all()
	template = loader.get_template('disease/index1.html')
	context = {
		'obj' : d ,
	}
	
	  
	return HttpResponse(template.render(context, request))


def detail(request, id):

	
	try:
		d = Disease.objects.get(key=int(id))
		
		
	except:
		raise Http404("Disease doesn't exist")
	
	template = loader.get_template('disease/index.html')
	context = {
		'obj' : d ,
	}

	return HttpResponse(template.render(context, request))

