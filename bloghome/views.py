from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def home(request):
  blog=Blog.objects.all()
  content={
               'blog':blog
  }
 
 
  return render (request,'home.html',content)

def about(request):
  return render (request,'about.html')
def contact(request):
  return render (request,'contact.html')
def content(request,id):
  blog=Blog.objects.get(id=id)
  contexnt={
               'blog':blog
  }

  return render(request,'blogcontent.html',contexnt)
def signup(request):
  if request.method=="POST":

   fname=request.POST.get('name')
   email=request.POST.get('email')

   password=request.POST.get('password')

   user = User.objects.create_user(first_name=fname,username=email,email=email, password=password)
 
   user.save()
   return redirect(log_in)

  return render(request,'signup.html')
def log_in(request):
  if request.method=="POST":


   email=request.POST.get('email')

   password=request.POST.get('password')
   user =authenticate(request, username=email, password=password)
  
   if user is not None:
      login(request,user)
   else:
     pass
   return redirect("home")


 
  return render(request,'login.html')
def log_out(request):
    logout(request)
    return redirect("home")


