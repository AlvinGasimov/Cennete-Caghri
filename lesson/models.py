from django.db import models
from django.utils.text import slugify

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
    description = models.TextField(verbose_name = 'Açıklama')
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