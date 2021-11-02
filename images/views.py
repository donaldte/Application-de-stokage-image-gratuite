from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Categories, Images, UserImages, Contact
from django.core.paginator import Paginator
from .form import FormContact


# Create your views here.

def index(request):
    image = Images.objects.all()
    value = request.GET.get('name')
    if value != '' and value is not None:
        image = Images.objects.filter(name__icontains=value)
    card = Categories.objects.all()
    paginator = Paginator(image, 8)
    page = request.GET.get('page')
    images = paginator.get_page(page)    
    content = {
        'images':images,
        'card':card,
            }
      
    return render(request, 'images/index.html', content )


def categories(request, id):
    card = Categories.objects.all()
    category = Categories.objects.get(pk=id)
    images = Images.objects.filter(category=category)
   
    content = {
        'images':images,
        'card':card,
            }
    return render(request, 'images/index.html', content )


def userImage(request):
    if request.method=='POST':
        name = request.POST.get('name')
        image = request.POST.get('image')
        img=UserImages(name=name, image=image)
        img.save()
                
    return render(request, 'base.html') 


def contact(request):
    if request.POST:
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('merciemagefrom')
        else:
            form = FormContact(request.POST)
    else:
        form = FormContact()
    return render(request, 'images/contact.html', {'form':form})              

def merci(request):
    contact = Contact.objects.all()[:1]
    print(contact)
    for element in contact:
        name=element.name
    return render(request, 'images/merci.html', {'name':name})    



                

