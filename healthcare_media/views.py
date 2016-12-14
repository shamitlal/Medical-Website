from django.shortcuts import render

# Create your views here.


def healthcare_media(request):
    return render(request, 'healthcare_media/healthcare_media.html', {})
