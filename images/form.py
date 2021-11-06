from django import forms
from django.contrib.auth.models import User
from .models import Contact, UserModel
from django.contrib.auth.forms import UserCreationForm


class FormContact(forms.ModelForm):
    class Meta():
        model = Contact

        fields = ['name', 'email', 'text']

        labels = {
            'name':'Votre nom',
            'email':'Addresse email',
            'text':'Message'
        }

        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':75, 'placeholder':'Entrez votre message ici.'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
        
class AuthenForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class InitForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['biographie']  
        widgets ={
            'biographie':forms.Textarea(attrs={'class':'form-control' ,'cols':80, 'rows':2, 'placeholder':'Je suis developeur java, python.' })
        }      
       