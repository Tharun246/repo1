from django.shortcuts import render

# Create your views here.
def home(request): 

    return render(request,"val.html")
def validate(request): 

    a=request.POST['un']
    b=request.POST['pwd']
    if a=='tharun' and b=='tarun123': 
        return render(request,'status.html',{'status':'Success'})
    else: 
          return render(request,'status.html',{'status':'Failed'}) 