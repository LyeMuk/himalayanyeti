from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.models import User
from . forms import articleform
from mainapp.models import article, label, categories

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, "mainapp/index.html")

def donation(request):
    return render(request, "mainapp/donation.html")

def help(request):
    contex={}
    object_list = article.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 6) # 6 employees per page
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    contex['page_obj']=page_obj
    return render(request, "mainapp/helpt.html", contex)

def userlogin(request):
    contex={'Alert':''}
    if request.method=='POST':
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username= username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                contex['Alert']="Login Credentials could not match/ wrong credentials"
        return render(request, "mainapp/login.html", contex)     
    return render(request, "mainapp/login.html", contex)

def userlogout(request):
    request.session.clear()
    logout(request)
    return redirect(home)

def createuser(request):
    pass