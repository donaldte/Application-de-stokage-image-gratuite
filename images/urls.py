from django.urls import path
from images.views import index, categories, merci, userImage, contact

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:id>', categories, name='categories'),
    path('envoyerimage', userImage, name='create'),
    path('sendmessageer', contact, name='contact'),
    path('merciemagefrom', merci, name='merci'),
    
]