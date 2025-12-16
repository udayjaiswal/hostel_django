from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')
def home(request):
    return render(request, 'main/index.html')

def find(request):
    return render(request, 'main/find.html')

def list_hostel(request):
    return render(request, 'main/list.html')

def contact(request):
    return render(request, 'main/contact.html')

def sorry(request):
    return render(request, 'main/sorry.html')

def login(request):
    return render(request, 'main/login.html')


from .models import Contact
from django.shortcuts import render, redirect

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            state=request.POST.get('state'),
            city=request.POST.get('city'),
            work=request.POST.get('work'),
        )
        return redirect('contact')

    return render(request, 'main/contact.html')
