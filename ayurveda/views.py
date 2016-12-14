from django.shortcuts import render

# Create your views here.


def ayurveda(request):
    return render(request, 'ayurveda/ayurveda.html', {})
