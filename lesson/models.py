from django.db import models
from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from base.models import Subscribe
from ckeditor.fields import RichTextField

class LessonCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name = 'Kategori İsmi')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name = 'Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Oluşturulma Tarihi')
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    def lesson_count(self):
        return self.lessons.count()
    
    class Meta:
        verbose_name = 'Ders Kategorisi'
        verbose_name_plural = 'Ders Kategorileri'
        
        
class Lesson(models.Model):
    category = models.ForeignKey(LessonCategory, on_delete=models.CASCADE, related_name='lessons', verbose_name = 'Kategori')
    title = models.CharField(max_length=200, verbose_name = 'Ders İsmi')
    description = RichTextField(verbose_name = 'Açıklama')
    author = models.CharField(max_length=100, verbose_name = 'Yazar')
    video_url = models.URLField(verbose_name = 'Video URL')
    image = models.ImageField(upload_to='lesson/', verbose_name = 'Resim')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name = 'Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Oluşturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Ders'
        verbose_name_plural = 'Dersler'
        
        
@receiver(post_save, sender=Lesson)
def send_email_on_new_article(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscribe.objects.all()

        for subscriber in subscribers:
            subject = 'Yeni Ders Yayınlandı'
            message = render_to_string(
                'lesson/message.html',
                {
                    'lesson_title': instance.title,
                }
            )
            send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email],
            html_message=message, 
        )