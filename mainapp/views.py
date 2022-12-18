from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "mainapp/index.html")

def donation(request):
    return render(request, "mainapp/donation.html")

def help(request):
    return render(request, "mainapp/help.html")
