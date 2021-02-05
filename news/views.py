from django.shortcuts import render,redirect
from news.models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,"index.html")


def validate(request):
    un=request.POST.get("un")
    pas=request.POST.get("pass")
    q=Users.objects.get(usrname=un,password=pas)
    if q and q.ustype:
        return render(request,"insert.html")
    elif q or q.ustype:
        return redirect("listing")
    else:
        return messages.error(request,"Invalid User")


def listing(request):
    qs=Content.objects.all()
    return render(request,"listing.html",{"data":qs})


def insert(request):
    return render(request,"insert.html")


def insertdata(request):
    title=request.POST.get("title")
    content=request.POST.get("content")
    image=request.FILES["img"]
    Content(title=title,content=content,image=image).save()
    return redirect("insert")


def newusr(request):
    un=request.POST.get("un")
    password=request.POST.get("pass")
    utype=request.POST.get("type")
    if utype=="writer":
        Users(usrname=un,password=password,ustype=True).save()
    else:
        Users(usrname=un, password=password).save()
    return render(request,"index.html")


def create(request):
    return render(request,"create.html")

