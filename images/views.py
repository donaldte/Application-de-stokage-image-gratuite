from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Categories, Images, UserImages, Contact
from django.core.paginator import Paginator
from .form import FormContact, AuthenForm, InitForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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

@login_required
def userImage(request):
    if request.method=='POST':
        image = request.POST.get('image',)
        description = request.POST.get('description',)
        username = request.POST.get('username',)
        userImage =UserImages(image=image, description=description, name=username)
        if userImage:
            userImage.save()
        else:
            HttpResponse("<h3 style='text-align: center'>une erreur a ete emise s'il vous plait veillez reesayer. </h3>")    
        
        return HttpResponseRedirect('merciemagefrom')            
    return render(request, 'base.html') 

def merciimage(request):
    return render(request, 'images/mercimage.html')    


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

def register(request):
    if request.POST:
        form = AuthenForm(request.POST)
        form1 = InitForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save()
            final = form1.save(commit=False)
            final.user = user
            final.save()

            return HttpResponseRedirect('login')
        else:
            print(form.errors, form1.errors)

    else:
        form = AuthenForm()    
        form1 = InitForm()       
    return render(request, 'images/resgister.html', {'form':form, 'form1':form1})


def userLogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("vous n'est pas active sur ce site")
        else:
            return HttpResponse("<h3 style='color:red; text-align:center'> votre mot de passe et nom d'utilisateur ne coinsident pas<br><a href='login' style='color:green'>Ressayez</a></h3>")                
    else:
        return render(request, 'images/login.html')    

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

                

