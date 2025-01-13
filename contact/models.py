from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ad Soyad')
    email = models.EmailField(verbose_name='E-posta')
    phone = models.CharField(max_length=50, verbose_name='Telefon Numarası')
    subject = models.CharField(max_length=300, verbose_name='Konu')
    message = models.TextField(verbose_name='Mesaj')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Olusturulma Tarihi')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'İletisim'
        verbose_name_plural = 'İletisimler'