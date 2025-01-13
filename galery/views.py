from django.shortcuts import render
from .models import Galery
from django.core.paginator import Paginator

def galeries(request):
    
    galeries = Galery.objects.all().order_by('-created_at')
    paginator = Paginator(galeries, 15)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'galeries' : galeries,
    }
    
    return render(request, 'galery/galery.html', context)