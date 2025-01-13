from django.shortcuts import render, get_object_or_404
from .models import ArticleCategory, Article
from django.core.paginator import Paginator
from django.db.models import Q
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

def articles(request):
    articles = Article.objects.all().order_by('-created_at')
    search_query = request.GET.get('search', '')
    
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query) | Q(author__icontains=search_query)
        )
        
    paginator = Paginator(articles, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'articles' : articles,
    }
    
    return render(request, 'article/articles.html', context)


def article_detail(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    categories = ArticleCategory.objects.all().order_by('-created_at')
    last_4_articles = Article.objects.all().order_by('-created_at')[:4]
    
    context = {
        'article': article,
        'categories' : categories,
        'last_4_articles' : last_4_articles
    }
    return render(request, 'article/article-detail.html', context)


def article_by_category(request, category_slug):
    
    category = get_object_or_404(ArticleCategory, slug=category_slug)
    articles = Article.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(articles, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'articles': articles,
        'page_obj' : page_obj
    }
    
    return render(request, 'article/article-category.html', context)


def set_language(request, language):
    if language not in dict(settings.LANGUAGES):
        return HttpResponseRedirect("/")

    referer = request.META.get("HTTP_REFERER", "/")
    try:
        view = resolve(urlparse(referer).path)
        translation.activate(language)
        app_name = view.app_name if hasattr(view, 'app_name') else None
        view_name = f"{app_name}:{view.url_name}" if app_name else view.url_name

        response = HttpResponseRedirect(
            reverse(view_name, args=view.args, kwargs=view.kwargs)
        )
    except Resolver404:
        response = HttpResponseRedirect("/")
    
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response