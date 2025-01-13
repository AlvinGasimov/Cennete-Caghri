from django.shortcuts import render
from .forms import SubscribeForm
from django.shortcuts import redirect
from django.contrib import messages

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


def error(request):
    return render(request, 'base/404.html')