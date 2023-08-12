from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def reg(request): 
    if request.method=='POST': 
        first=request.POST.get('first','')
        last=request.POST.get('last','')
        email=request.POST.get('email','')
        username=request.POST.get('username','')
        password=request.POST.get('pwd1','') 
        user = User.objects.create_user(first_name=first, last_name=last, email=email, username=username, password=password)
        user.save()
        print("user created")
        return redirect('/')

    else:
        return render(request,'register.html')
