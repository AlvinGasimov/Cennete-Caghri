from django.contrib import admin
from .models import ArticleCategory, Article

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count', 'slug', 'created_at')
    
    def article_count(self, obj):
        return obj.article_count()
    article_count.short_description = 'Makale Sayısı'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'slug', 'created_at')
    search_fields = ('title', 'author', 'category')