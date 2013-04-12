from django.shortcuts import render_to_response
from django.shortcuts import redirect, render
from ad.models import Ad, AdForm, City, Category
from userprof.models import Profile, UserCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
 
def home(request):
    citys = City.objects.all()
    return render_to_response("home.html", {'citys': citys,}, RequestContext(request))

def registration(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        form.save()
        user = authenticate(username = username, password = password)
        if user is not None:
            user.backend='django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/'+user.profile.city.name)
        return redirect('/')
    else:
        form = UserCreateForm()
        return render_to_response("registration.html", {'form' : form}, RequestContext(request))
    

def archive(request):
    ads = Ad.objects.all()
    return render_to_response("archive.html",{'ads': ads,}, RequestContext(request))
    
def addition(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            addit = form.save(commit=False)
            addit.user = request.user
            addit.save()
            return redirect('/archive/') 
    else:
        form = AdForm()
    return render_to_response("addition.html",{'form' : form,}, RequestContext(request))

def userlogout(request):
    logout(request)
    return redirect('/')

def cityarchive(request, urlcity):
    city = City.objects.get(name = urlcity)
    ads = city.ad_set.all()
    return render_to_response("cityarchive.html", {'ads' : ads, 'city' : city,}, RequestContext(request))
    
def categoryarchive(request, urlcity, urlcategory):
    city = City.objects.get(name = urlcity)
    category = Category.objects.get(name = urlcategory)
    ads = city.ad_set.all()
    ads = ads.filter(category = category,)
    return render_to_response("categoryarchive.html", {'ads' : ads, 'city' : city, 'category' : category}, RequestContext(request))

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/'+user.profile.city.name)
        else:
            return render_to_response("home.html", {'user' : 'Wrong user'})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form' : form})
