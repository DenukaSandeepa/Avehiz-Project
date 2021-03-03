from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate


def login(request):
  if request.method == 'POST':

    user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])

    if user is not None:
      auth.login(request, user)
      return redirect('index')
    else:
      return render(request,'accounts/login.html',{'error':'Invalid Email Or Password'})
  else:
    return render(request, 'accounts/login.html')



def signup(request):

  if request.method == 'POST':

    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    if len('password')>4:
          if password == cpassword:
              try:
                  user = User.objects.get(username = username)
                  return render(request, 'accounts/signup.html',{'error':'Username Alrady In Use'})
              except User.DoesNotExist:
                  user = User.objects.create_user(username,email,password)
                  auth.login(request,user)
                  return redirect('index')
          else:
              return render(request, 'accounts/signup.html',{'error':'Passwords Must Match'})
    else:
        return render(request, 'accounts/signup.html',{'error':'Passwords Must Be Least 5 Characters'})
  else:
    return render(request, 'accounts/signup.html')
