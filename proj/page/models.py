from django.db import models

class change(models.Model): 
    name = models.CharField(max_length=100) 
    img = models.ImageField(upload_to="pics")
    price = models.IntegerField()
    desc = models.TextField() 

