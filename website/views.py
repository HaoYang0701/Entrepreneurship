from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'Home.html', {})

def agri(request):
    return render(request,'Agri.html',{})

def contact(request):
    return render(request,'Contact.html',{})


def cust(request):
    return render(request,'Cust.html',{})


def oper(request):
    return render(request,'Oper.html',{})

def risk(request):
    return render(request,'Risk.html',{})

def trans(request):
    return render(request,'Trans.html',{})

