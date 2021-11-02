from django import forms
from django.forms import widgets
from .models import Contact


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
            'text':forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':75, 'placeholder':'Entrez votre message ici.'})
        }
        

       