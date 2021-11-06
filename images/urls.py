from django.urls import path
from images.views import index, categories, merci, userImage, contact, register, userLogin, userLogout, merciimage

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:id>', categories, name='categories'),
    path('envoyerimage', userImage, name='create'),
    path('register', register, name='register'),
    path('login', userLogin, name='login'),
    path('logout', userLogout, name='logout'),
    path('sendmessageer', contact, name='contact'),
    path('mercicontactfrom', merci, name='merci'),
    path('merciemagefrom', merciimage, name='mercimage'),
    
]