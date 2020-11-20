from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render 
from django.template.loader import get_template


def inicio(request):  
    return render(request, 'index.html')

def perfil(request):  
    return render(request, 'profile.html')

def bar(request):  
    return render(request, 'bar.html')

def login(request):  
    return render(request, 'login.html')

def register(request):  
    return render(request, 'register.html')

def categories(request):  
    return render(request, 'categories.html')


def publicación(request):  
    return render(request, 'Vista_publicación.html')