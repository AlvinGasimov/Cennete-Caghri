from django.urls import path
from .views import articles, article_detail, article_by_category, set_language

app_name = 'article'

urlpatterns = [
    path('', articles, name='articles'),
    path('<slug:article_slug>/', article_detail, name='article_detail'),
    path('kategori/<slug:category_slug>', article_by_category, name='article_by_category'),
    path("set_language/<str:language>", set_language, name="set-language"),
]