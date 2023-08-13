from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.db import IntegrityError
# Create your views here.
def reg(request): 
    if request.method=='POST': 
            first=request.POST.get('first','')
            last=request.POST.get('last','')
            email=request.POST.get('email','')
            username=request.POST.get('username','')
            password1=request.POST['pwd1']
            password2=request.POST['pwd2']

            if password1==password2:
                
                if User.objects.filter(username=username).exists(): 
                    print("username already taken")

                elif User.objects.filter(email=email).exists():
                    print("email is  already registered") 

                else:
          
                        user=User.objects.create_user(first_name=first,last_name=last,email=email,username=username,password=password1)
                        user.save();
                        print("user created")
                        return redirect('/')
            else: 
                print("password is not matched")
    else:
        return render(request,'register.html')
       
    return redirect('/')