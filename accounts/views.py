from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['password2']:
            try:
                user= User.objects.get(username=request.POST['Username'])
                return render(request,'accounts/signup.html',{'error':'Username is already taken, Try a Different One🙂'})
            except User.DoesNotExist:
                user= User.objects.create_user(username=request.POST['Username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Passwords must match'})
    else:
        return render(request,'accounts/signup.html')
def login(request):
    return render(request,'accounts/login.html')
def logout(request):
    return render(request,'accounts/signup.html')
