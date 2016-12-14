from django.shortcuts import render, redirect

# Create your views here.


def video_chat(request):
    if not request.user.is_authenticated():
        return redirect('/medworld/')
    print request.user.id
    return render(request, 'video_chat/video_chat.html', {})
