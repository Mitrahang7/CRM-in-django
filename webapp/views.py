from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Client





def home(request):
   if request.user.is_authenticated:
    clients= Client.objects.all()

   else:
      messages.error(request, ' Sorry You must be logged in  to view this page')
      return redirect('login')

   return render(request,'home.html', {'clients':clients})


def client_detail(request, pk):
    if request.user.is_authenticated:
      client= Client.objects.get(pk=pk)
    
    else:
      messages.error(request, ' Sorry You must be logged in  to view this page')
      return redirect('login')

    return render(request,'client_detail.html', {'client':client})

def client_delete(request,pk):
  if request.user.is_authenticated:
    client= Client.objects.get(pk=pk)
    client.delete()
    messages.success(request,"Successfully deleted the client ...")
    return redirect('home')

  
  else:
    messages.error(request, ' Sorry You must be logged in  to view this page')
    return redirect('login')
  
def add_client(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      full_name= request.POST.get('full_name')
      email= request.POST.get('email')
      phone= request.POST.get('phone')
      address= request.POST.get('address')
      city= request.POST.get('city')
      state= request.POST.get('state')
      zipcode= request.POST.get('zipcode')

      if Client.objects.filter(email=email,phone=phone).exists():
        messages.error(request,"The user of this email and phone already exits")
        return redirect('add_client')

      Client.objects.create(full_name=full_name,email=email,phone=phone,address=address,city=city,state=state,zipcode=zipcode)

      messages.success(request,"Client is added succesfully...")
      return redirect('home')
    
    return render (request, 'client_add.html')

  else:
    messages.error(request, ' Sorry You must be logged in  to view this page')
    return redirect('login')
  

def client_update(request,pk):
  if request.user.is_authenticated:

    client = Client.objects.filter(pk=pk).first()

    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")

        client.full_name = full_name
        client.email = email
        client.phone = phone
        client.address = address
        client.city = city
        client.state = state
        client.zipcode = zipcode
        client.save()    

        messages.success(request, "Your details is updated successfully!")
        return redirect("client_detail", pk=pk)


    return render(request,'client_update.html', {"client_id": pk,'client':client})
  
  else:
    messages.error(request, ' Sorry You must be logged in  to view this page')
    return redirect('login')




  
  

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



 
