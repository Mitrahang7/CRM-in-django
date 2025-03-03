from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User




def home(request):
  return render(request,'home.html', {})


def login_user(request):
  if request.method == 'POST':
    username= request.POST['username']
    password= request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      messages.success(request,"You are Successfully logged in...")
      return redirect('home')
    
    else:
      messages.error(request, ' Please Validate your details again')
      return redirect('login')

  return render(request, 'login.html')

def logout_user(request):
  logout(request)
  messages.success(request," You are logout succesfully....")
  return redirect ('login')

def register(request):
  if request.method == 'POST':
    username=request.POST.get('username')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email= request.POST.get('email')
    password1=request.POST.get('password1')
    password2=request.POST.get('password2')

    if password1 != password2:
      messages.error(request,"Password didn't match.Try again..")
      return redirect('register')
    
    if User.objects.filter(username=username):
      messages.error(request,"Username is already taken.Try another name..")
      return redirect('register')
    
    if User.objects.filter(email=email):
      messages.error(request,"This Email is already taken.Try another email..")
      return redirect('register')
    
    user= User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password1)

    user.save()

    login(request,user)
    messages.success(request,"Your account is created succesfully ...")
    return redirect ('home')
  
  else:
    return render(request,'register.html')



 
