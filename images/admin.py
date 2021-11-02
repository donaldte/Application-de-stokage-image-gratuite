from django.contrib import admin
from .models import  Categories, Images, UserImages, Contact

# Register your models here.
admin.site.register(Categories)
admin.site.register(Images)
admin.site.register(UserImages)
admin.site.register(Contact)
