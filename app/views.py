from django.shortcuts import render
from .forms import register, customLogin
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from .models import Category, Photo

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



# second part
def home(request):
    category = request.GET.get('category')
    user = request.user

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    return render(request, 'gallery.html', context={'categories':categories, 'photos':photos})




def addPhoto(request):
    user = request.user
    # categories = user.category_set.all()
    
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('images')
        print(data) ,print(image)

        if data['category'] != 'none':
            category = Category.objects.get(name=data['category'])
        
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(user=user,name=data['category_new'])
        
        else:
            category = None
        
        photo = Photo.objects.create(
            category = category,
            image = image
        )
        return HttpResponseRedirect('/')

    return render(request, 'add.html', context={"categories":categories})




def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')