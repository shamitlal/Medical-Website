from django.shortcuts import render

# Create your views here.


def homeopathy(request):
    return render(request, 'homeopathy/homeopathy.html', {})
