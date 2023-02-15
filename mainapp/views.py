from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.models import User
from . forms import articleform
from mainapp.models import article, label, categories, subscriber

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

# Imports to send email
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Global variables

labelvalue=0                            #used in help function to keep track of filter in help section

# Create your views here.

def sendWelcomeMail(mail):
    send_to=[]
    send_to.append(mail)
    contex={}
    contex['mailid']=mail.split('@')[0]
    html_content = render_to_string("mainapp/emailtemplate/welcome.html", contex)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Thanks for Subscribing Himalayan Yeti Foundation",
        text_content,
        settings.EMAIL_HOST_USER ,
        send_to
    )
    email.attach_alternative(html_content, 'text/html')
    print(email)
    email.send()
    return 

def home(request):
    contex={}
    if request.method == 'POST' and 'scrubmail' in request.POST:
        scrubmail = request.POST['scrubmail']
        mail = subscriber.objects.create(mail=scrubmail)
        sendWelcomeMail(scrubmail)
        mail.save()
    eventlist = article.objects.filter(category=6).order_by('-postdate')[0:3]
    contex['eventlist']=eventlist
    return render(request, "mainapp/index.html", contex)

def donation(request):
    return render(request, "mainapp/donation.html")

def help(request):
    contex={}
    global labelvalue
    labelvalue = int(request.GET.get('label', labelvalue))
    if labelvalue==0:
        object_list = article.objects.filter(category=5).order_by('-postdate') # category 5 belongs to help/blog
    else:
        object_list = article.objects.filter(label=labelvalue).order_by('-postdate')

    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 6) # 6 article per page
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    contex['page_obj']=page_obj
    labellist = label.objects.filter(parentcategory=5) # parentcategory 5 belongs to help
    contex['labellist']=labellist
    contex['labelvalue']=labelvalue

    return render(request, "mainapp/help.html", contex)

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

@login_required(login_url='/userlogin')
def addarticle(request):
    contex={}
    if request.method == 'POST':
        form = articleform(request.POST,request.FILES)
        if form.is_valid():
            form.author = request.user.id     
            lbl = label.objects.get(lid=request.POST['label'])
            if int(request.POST['category']) == int(lbl.parentcategory.cid):
                form.save()
                return redirect(help)
            else:
                contex['Alert']="Input category and label category dont match please create new or change accordingly"
    artform = articleform()
    contex['artform']=artform
    return render(request, "mainapp/addarticle.html", contex)

def about(request):
    contex={}
    project = article.objects.filter(category=7).order_by('-postdate')[0:6]
    contex['project'] = project
    return render(request, "mainapp/about.html", contex)

@login_required(login_url='/userlogin')
def deletearticle(request, num):
    instance = article.objects.get(bid=num)
    instance.delete()
    return redirect(help)

def viewarticle(request, num):
    contx={}
    instance = article.objects.get(bid=num)
    contx['article']=instance
    return render(request, "mainapp/viewarticle.html", contx)

@login_required(login_url='/userlogin')
def updatearticle(request, pk):
    contex={}
    blog_post = get_object_or_404(article, bid=pk)
    if request.method == 'POST':
        form = articleform(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            lbl = label.objects.get(lid=request.POST['label'])
            if int(request.POST['category']) == int(lbl.parentcategory.cid):
                form.save()
                return redirect('viewarticle', num=pk)
            else:
                contex['Alert']="Input category and label category dont match please create new or change accordingly"
    
    form = articleform(instance=blog_post)
    contex['artform']=form
    return render(request, "mainapp/addarticle.html", contex)


def contact(request):
    contex={}
    return render(request, "mainapp/contact.html", contex)


def government(request):
    contex={}
    return render(request, "mainapp/government.html", contex)


def organisation(request):
    contex={}
    return render(request, "mainapp/organisation.html", contex)

def institute(request):
    contex={}
    return render(request, "mainapp/institute.html", contex)


def individual(request):
    contex={}
    return render(request, "mainapp/individual.html", contex)

def csr(request):
    contex={}
    return render(request, "mainapp/csr.html", contex)

def getinvolved(request):
    contex = {}
    return render(request, "mainapp/getinvolved.html", contex)

def focusArea(request):
    contex={}
    return render(request, "mainapp/focusArea.html", contex)

def testimonial(request):
    contex={}
    return render(request, "mainapp/testimonial.html", contex)
