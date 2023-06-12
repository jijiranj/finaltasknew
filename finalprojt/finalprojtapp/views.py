from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import District,contactdetails



def demo(request):
    obj = District.objects.all()
    return render(request,"index.html",{'brnch':obj})


def login(request):
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)

      if user is not None:
         auth.login(request,user)
         return redirect('/new')
      else:
          messages.info(request, "Invalid Credentials")
          return redirect('/login')
   return render(request,"login.html")



def detail(request,branch_id):
    branch=Branches.objects.get(id=branch_id)
    return render(request,"detail.html",{'branch':branch})




def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       password1 = request.POST['password1']
       if not username:
          messages.info(request,"Empty username")
          return redirect('/register')
       else:
           if password == password1 :
              if User.objects.filter(username=username).exists():
                 messages.info(request,"Username Taken")
                 return redirect('/register')
              else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('/login')
           else:
                messages.info(request,"password not matching")
                return redirect('/register')
    return render(request,"register.html")
# def formnew(request):
#     branch2 = Branches.objects.all()
#     return render(request,"formnew.html",{'branch2':branch2})


def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):
    return render(request,"new.html")



def getdata(request):
    district = District.objects.all()
    brcontext = contactdetails.objects.all()
    if request.method == 'POST':
       messages.info(request, "Application  Accepted")
    return render(request,'check.html', {'district': district,'brcontext': brcontext})





def registerform(request):
    if request.method == 'POST':
       messages.info(request,"Application Accepted")
    return render(request,"check.html")



