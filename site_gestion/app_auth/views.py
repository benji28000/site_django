from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
def login_site(request):
    if request.method== "POST":
        form = login_Form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data['pwd']
            user=authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Authentifiaction non valide")
                return render(request,'login.html',{'form':form})
        else:
            return render(request,'login.html',{'form':form})
    else:
        form=login_Form()
        return render(request,'login.html',{"form":form})
    
def register(request):
    if request.method=="POST":
        form=register_Form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data['pwd']
            user=User.objects.create_user(username=username,password=pwd)
            if user is not None:
                return redirect('login-site')
            else:
                messages.error(request,"La création du compte n'a pas fonctionnée")
                return render(request,'register.html',{'form':form})
        
        else:
            return  render(request,'register.html',{'form':form})
    
    form= register_Form()
    return render(request,'register.html',{'form':form})

def deconnexion(request):
    logout(request)
    return redirect('login-site')
    

