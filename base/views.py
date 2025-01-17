from django.shortcuts import render
from .forms import SubscribeForm, ContactForm
from django.shortcuts import redirect
from django.contrib import messages
from .models import Galery
from django.core.paginator import Paginator

def index(request):
    
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Başarıyla abone olundu!!!")
            return redirect('base:index')
    else:
        form = SubscribeForm()
        
    context = {
        'form' : form
    }
    
    return render(request, 'base/index.html', context)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Mesajınız başarıyla gönderildi!")
            return redirect('base:contact')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    return render(request, 'base/contact.html', context)


def galeries(request):
    
    galeries = Galery.objects.all().order_by('-created_at')
    paginator = Paginator(galeries, 15)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'galeries' : galeries,
    }
    
    return render(request, 'base/galery.html', context)

def error(request):
    return render(request, 'base/404.html')