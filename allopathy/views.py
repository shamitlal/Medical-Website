from django.shortcuts import render

# Create your views here.


def allopathy(request):
    return render(request, 'allopathy/allopathy.html', {})
