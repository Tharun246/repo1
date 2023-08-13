from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('nature.urls')),
    path('admin/', admin.site.urls),
]
