from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request): 
    return HttpResponse("<center><h2>Welcome fo home page</h2></center>")