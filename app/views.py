from django.shortcuts import render
from .forms import register, customLogin

# Create your views here.
def home(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def loginUser(request):
    page = 'login'
    form = customLogin()
    return render(request, 'login_register.html', context={'form':form, 'page':page})

def registerUser(request):
    page = 'register'
    form = register()
    return render(request, 'login_register.html',context={'form':form, 'page':page})

def addPhoto(request):
    return render(request, 'add.html')