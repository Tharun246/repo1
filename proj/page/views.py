from django.shortcuts import render
from .models import change
# Create your views here.
def home(request): 
    '''
    c1=change()
    c1.name="mumbai"
    c1.desc="city that never sleeps"
    c1.price=115
    c1.img='templatemo_header_1.jpg'

    c2=change()
    c2.name="Hyderabad"
    c2.desc="sunrisers thappa anni ishtame"
    c2.img='templatemo_header_2.jpg'
    c2.price=255

    c3=change()
    c3.img='templatemo_header_3.jpg'
    c3.name="Miller planet"
    c3.desc="Don't spend too much time here"
    c3.price=345

    c4=change()
    c4.name="bangalore"
    c4.desc="ee saala ayina kodithe....."
    c4.price=555
    c4.img='templatemo_slide_2.jpg'

    dests=[c1,c2,c3,c4]
    ''' 
    dests= change.objects.all()
    return render(request,'index.html',{'des':dests})