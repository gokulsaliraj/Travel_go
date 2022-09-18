from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages ,auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        pswd=request.POST['pswd']
        user=auth.authenticate(username=username,password=pswd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pswd = request.POST['pswd']
        pswd1 = request.POST['pswd1']

        if pswd==pswd1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
#                messages.info(request,"email taken")
                messages.info(request,"email taken")
                return redirect('register')

            else:
              user=User.objects.create_user(username=username,password=pswd,email=email,first_name=first_name,last_name=last_name)

            user.save();
            return redirect('login')
            print("user registerd")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
