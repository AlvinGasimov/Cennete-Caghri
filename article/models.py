from django.db import models
from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from base.models import Subscribe
from ckeditor.fields import RichTextField

class ArticleCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Makale Kategori Adı')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Makale Kategori Oluşturulma Tarihi')
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def article_count(self):
        return self.articles.count()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Makale Kategorileri'
        

class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='Makale Kategorisi', related_name='articles')
    title = models.CharField(max_length=200, verbose_name='Makale Başlığı')
    description = RichTextField(verbose_name = 'Makale Açıklaması')
    author = models.CharField(max_length=200, verbose_name='Makale Yazarı')
    image = models.ImageField(upload_to='article_images/', verbose_name='Makale Resmi')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Makale Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Makale Güncellenme Tarihi')
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Makaleler'
        

@receiver(post_save, sender=Article)
def send_email_on_new_article(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscribe.objects.all()

        for subscriber in subscribers:
            subject = 'Yeni Makale Yayınlandı'
            message = render_to_string(
                'article/message.html',
                {
                    'article_title': instance.title,
                }
            )
            send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email],
            html_message=message, 
        )