from django.db import models

# Create your models here.
class Users(models.Model):
    uid=models.IntegerField(auto_created=True,primary_key=True)
    usrname=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    ustype=models.BooleanField(default=False)

class Content(models.Model):
    title=models.CharField(max_length=80)
    content=models.CharField(max_length=7000)
    image=models.ImageField()

