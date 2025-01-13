from django.db import models

class GeneralItem(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Genel Bilgiler Başlığı')
    description = models.TextField(verbose_name = 'Açıklama')
    email = models.EmailField(verbose_name = 'E-posta')
    address = models.TextField(verbose_name = 'Adres')
    main_phone_number = models.CharField(max_length = 50, verbose_name = 'En çok kullanılan telefon numarası')
    favicon = models.ImageField(upload_to = 'favicon', verbose_name = 'Favicon')
    navbar_img = models.ImageField(upload_to='navbar_img', verbose_name = 'Navbar Resmi')
    footer_img = models.ImageField(upload_to='footer_img', verbose_name = 'Footer Resmi')
    facebook = models.URLField(verbose_name = 'Facebook linki', null=True, blank=True)
    instagram = models.URLField(verbose_name = 'İnstagram linki', null=True, blank=True)
    twitter = models.URLField(verbose_name = 'Twitter linki', null=True, blank=True)
    youtube_1 = models.URLField(verbose_name = 'Youtube birinci linki', null=True, blank=True)
    youtube_2 = models.URLField(verbose_name = 'Youtube ikinci linki', null=True, blank=True)
    youtube_3 = models.URLField(verbose_name = 'Youtube üçüncü linki', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Genel Bilgiler'
 

class HomeSlider(models.Model):
    text_arabic = models.TextField(verbose_name = 'Metin (Arapça)')
    text_translation =  models.TextField(verbose_name = 'Metin (Çeviri)')
    source = models.CharField(max_length = 200, verbose_name = 'Kaynak')
    image = models.ImageField(upload_to = 'home_slider', verbose_name = 'Resim')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.source

    class Meta:
        verbose_name_plural = 'Ana Sayfa Sliderları'



class PageBanner(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Banner Baslığı')
    
    about_img = models.ImageField(upload_to='about_banner_img', verbose_name = 'Hakkımızda Banner Resmi')
    about_arabic_text = models.TextField(verbose_name = 'Hakkımızda Banner Metin (Arapça)')
 
    article_img = models.ImageField(upload_to='article_banner_img', verbose_name = 'Makale Banner Resmi')
    article_arabic_text = models.TextField(verbose_name = 'Makale Banner Metin (Arapça)')
    
    article_category_img = models.ImageField(upload_to='article_category_banner_img', verbose_name = 'Makale Detayları Banner Resmi')
    article_category_arabic_text = models.TextField(verbose_name = 'Makale Kategorisi Banner Metin (Arapça)')
    
    article_detail_img = models.ImageField(upload_to='article_detail_banner_img', verbose_name = 'Makale Detayları Banner Resmi')
    article_detail_arabic_text = models.TextField(verbose_name = 'Makale Detayları Banner Metin (Arapça)')

    lesson_img = models.ImageField(upload_to='lesson_banner_img', verbose_name = 'Ders Banner Resmi')
    lesson_arabic_text = models.TextField(verbose_name = 'Ders Banner Metin (Arapça)')
    
    lesson_detail_img = models.ImageField(upload_to='lesson_detail_banner_img', verbose_name = 'Ders Detayları Banner Resmi')
    lesson_detail_arabic_text = models.TextField(verbose_name = 'Ders Detayları Banner Metin (Arapça)')
    
    galery_img = models.ImageField(upload_to='galery_banner_img', verbose_name = 'Galeri Banner Resmi')
    galery_arabic_text = models.TextField(verbose_name = 'Galeri Banner Metin (Arapça)')
    
    contact_img = models.ImageField(upload_to='contact_banner_img', verbose_name = 'İletişim Banner Resmi')
    contact_arabic_text = models.TextField(verbose_name = 'İletişim Banner Metin (Arapça)')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sayfa Bannerları'
        

class Phone(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Telefon Numarası Başlığı')
    phone_number = models.CharField(max_length = 50, verbose_name = 'Telefon numarası')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Telefon Numaraları'
        
        
class IslamicConditions(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Şartın Başlığı')
    description = models.TextField(verbose_name = 'Şartın Açıklaması')
    icon = models.CharField(max_length=200, verbose_name = 'Şartın Simgesi (İkon)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'İslamın Şartları'
        
        
class About(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Hakkımızda Başlığı')
    description = models.TextField(verbose_name = 'Hakkımızda Açıklaması')
    image = models.ImageField(upload_to = 'about', verbose_name = 'Arkaplan Resmi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    class Meta:
        verbose_name_plural = 'Hakkımızda'
        
    def __str__(self):
        return self.title
    
    
class CommunityService(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Genel Hizmetler Başlığı')
    description = models.TextField(verbose_name = 'Genel Hizmetler Açıklaması')
    image = models.ImageField(upload_to = 'community_service', verbose_name = 'Arkaplan Resmi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Hizmet Bilgileri'
    
class Service(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Hizmetler Başlığı')
    description = models.TextField(verbose_name = 'Açıklama')
    icon = models.CharField(max_length = 200, verbose_name = 'Simge (İkon)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Hizmetler'
    
    
class Mission(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Görevler Başlığı')
    description = models.TextField(verbose_name = 'Açıklama')
    image = models.ImageField(upload_to = 'mission', verbose_name = 'Resim')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Görevler'
    
    
class SubMission(models.Model):
    mission = models.ForeignKey(Mission, on_delete = models.CASCADE, verbose_name = 'Görevler', related_name = 'submissions')
    title = models.CharField(max_length = 400, verbose_name = 'Görevler Başlığı')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Alt Görevler'
        
        
class Subscribe(models.Model):
    email = models.EmailField(verbose_name = 'E-posta')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Aboneler'