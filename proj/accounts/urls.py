from django.urls import path 
from . import views 

urlpatterns=[

    path('register',views.reg,name="name"),
    path('login',views.log,name="login"),
    path('logout',views.logg,name="logout"),
]