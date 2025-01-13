from django.db import models

class Galery(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Başlık')
    image = models.ImageField(upload_to='images/', verbose_name='Resim')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeriler'