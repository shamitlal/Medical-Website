#views.py
from login.form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
 
@csrf_protect
def register_login(request):
    if(request.method=='GET'):
        if request.user.is_authenticated():
            return redirect('/medworld/')
        form = RegistrationForm()
        variables = RequestContext(request, {
        'form': form,
        'msg':'',
        })
     
        return render_to_response(
        'registration/register.html',
        variables,
        )

    elif(request.method=='POST'):
        if request.POST.get("signup"):
            #print "signup"
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
                )
                new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
                if new_user is not None:
                    login(request, new_user)
                    return HttpResponseRedirect("/medworld/")
                else:
                    return HttpResponse('You are not authenticated')
            else:
                return render(request,'registration/register.html',{'msg':'invalid credentials supplied'})


        elif request.POST['pass'] is not None:
            username = request.POST.get('user')
            password = request.POST.get('pass')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/medworld/')
            else:
                return render(request,'registration/register.html',{'msg':'invalid credentials supplied'})



 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/medworld/')
