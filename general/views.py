from django.http import HttpResponse
from models import News
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import Http404

def index(request):
	d = News.objects.all()
	template = loader.get_template('general/index.html')
	context = {
		'obj' : d[:5] ,
		'endobj' : d[5:],
	}
	
	  
	return HttpResponse(template.render(context, request))
