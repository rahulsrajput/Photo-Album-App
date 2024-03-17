from django.shortcuts import render
from .forms import register, customLogin
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

# Create your views here.
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = customLogin(request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user_obj = authenticate(username=uname, password=upass)

                if user_obj is not None:
                    login(request,user_obj)
                    return HttpResponseRedirect('/')
                
        form = customLogin()
        
    return render(request, 'login_register.html', context={'form':form, 'page':page})


def registerUser(request):
    page = 'register'
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = register(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            
        form = register()
    
    return render(request, 'login_register.html',context={'form':form, 'page':page})


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')




def home(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def addPhoto(request):
    return render(request, 'add.html')