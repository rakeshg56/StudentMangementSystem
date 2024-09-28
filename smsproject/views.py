from django.http import HttpResponse
from django.shortcuts import render




def demofunction1(request ):
    return HttpResponse("<h3>PRACTICE</H3>")

def homefunction(request ):
    return render(request,"index.html")

def aboutfunction(request ):
    return render(request,"about.html")

def loginfunction(request ):
    return render(request,"login.html")

def contactfunction(request ):
    return render(request,"contact.html")

def facultylogin(request):
    return  render(request,"facultylogin.html")

def studentlogin(request):
    return  render(request,"studentlogin.html")

def frontpage(request):
    return  render(request,"fp.html")




