from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# page call methods
def index(request):
    return render(request,"auth/index.html",{})

def register_page(request):
    return render(request,"auth/register.html",{})

def reset_password_page(request):
    return render(request,"auth/reset_password.html",{})

def link_page(request):
    return render(request,"links.html",{})

def todo_list_page(request):
    return render(request,"todo-list.html",{})

def user_profile_page(request):
    return render(request,"user_profile.html",{})

def todo_detail_page(request):
    return render(request,"todo-detail.html",{})

def login_page(request):
    return render(request,"login.html",{})
