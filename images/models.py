from django.db import models
from django.contrib.auth.models import User 

    

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class Images(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    date_added = models.DateTimeField(auto_now=True) 
    category = models.ForeignKey(Categories, on_delete=models.CASCADE) 


    def __str__(self):
        return self.name


        
class UserImages(models.Model):
    name = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='userImages/', null=True, blank=True)
    description = models.TextField(default='unknow')
    date_added = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name 

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    text = models.TextField() 
    date = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ['-date']  

    def __str__(self):
        return self.name     


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biographie = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username
    


    