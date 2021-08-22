from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect('register')
        return redirect('/')
    else:


        return render(request,'reg.html')

