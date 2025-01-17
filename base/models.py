from turtle import mode
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class GeneralItem(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Genel Bilgiler Başlığı')
    description = RichTextField(verbose_name = 'Açıklama')
    email = models.EmailField(verbose_name = 'E-posta')
    address = RichTextField(verbose_name = 'Adres')
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
    text_arabic = RichTextField(verbose_name = 'Metin (Arapça)')
    text_translation =  RichTextField(verbose_name = 'Metin (Çeviri)')
    source = models.CharField(max_length = 200, verbose_name = 'Kaynak')
    image = models.ImageField(upload_to = 'home_slider', verbose_name = 'Resim')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.source

    class Meta:
        verbose_name_plural = 'Ana Sayfa Sliderları'



class PageBanner(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Banner Baslığı')
    
    about_title = models.CharField(max_length = 200, verbose_name = 'Hakkımızda Banner Başlığı')
    about_img = models.ImageField(upload_to='about_banner_img', verbose_name = 'Hakkımızda Banner Resmi')
    about_arabic_text = RichTextField(verbose_name = 'Hakkımızda Banner Metin (Arapça)')
 
    article_title = models.CharField(max_length = 200, verbose_name = 'Makale Banner Başlığı')
    article_img = models.ImageField(upload_to='article_banner_img', verbose_name = 'Makale Banner Resmi')
    article_arabic_text = RichTextField(verbose_name = 'Makale Banner Metin (Arapça)')
    
    article_category_title = models.CharField(max_length = 200, verbose_name = 'Makale Kategorisi Banner Başlığı')
    article_category_img = models.ImageField(upload_to='article_category_banner_img', verbose_name = 'Makale Kategorisi Banner Resmi')
    article_category_arabic_text = RichTextField(verbose_name = 'Makale Kategorisi Banner Metin (Arapça)')
    
    article_detail_title = models.CharField(max_length = 200, verbose_name = 'Makale Detayları Banner Başlığı')
    article_detail_img = models.ImageField(upload_to='article_detail_banner_img', verbose_name = 'Makale Detayları Banner Resmi')
    article_detail_arabic_text = RichTextField(verbose_name = 'Makale Detayları Banner Metin (Arapça)')

    lesson_title = models.CharField(max_length = 200, verbose_name = 'Ders Banner Başlığı')
    lesson_img = models.ImageField(upload_to='lesson_banner_img', verbose_name = 'Ders Banner Resmi')
    lesson_arabic_text = RichTextField(verbose_name = 'Ders Banner Metin (Arapça)')
    
    lesson_detail_title = models.CharField(max_length = 200, verbose_name = 'Ders Detayları Banner Başlığı')
    lesson_detail_img = models.ImageField(upload_to='lesson_detail_banner_img', verbose_name = 'Ders Detayları Banner Resmi')
    lesson_detail_arabic_text = RichTextField(verbose_name = 'Ders Detayları Banner Metin (Arapça)')
    
    galery_title = models.CharField(max_length = 200, verbose_name = 'Galeri Banner Başlığı')
    galery_img = models.ImageField(upload_to='galery_banner_img', verbose_name = 'Galeri Banner Resmi')
    galery_arabic_text = RichTextField(verbose_name = 'Galeri Banner Metin (Arapça)')
    
    contact_title = models.CharField(max_length = 200, verbose_name = 'İletişim Banner Başlığı')
    contact_img = models.ImageField(upload_to='contact_banner_img', verbose_name = 'İletişim Banner Resmi')
    contact_arabic_text = RichTextField(verbose_name = 'İletişim Banner Metin (Arapça)')
    
    subcsribe_title = models.CharField(max_length = 200, verbose_name = 'Abone Ol Banner Başlığı')
    subcsribe_img = models.ImageField(upload_to='subscribe_banner_img', verbose_name = 'Abone Ol Banner Resmi')
    subcsribe_description = models.TextField(verbose_name = 'Abone Ol Banner Kısa Açıklaması')
    
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
    description = RichTextField(verbose_name = 'Şartın Açıklaması')
    icon = models.CharField(max_length=200, verbose_name = 'Şartın Simgesi (İkon)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'İslamın Şartları'
        
        
class About(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Hakkımızda Başlığı')
    description = RichTextField(verbose_name = 'Hakkımızda Açıklaması')
    image = models.ImageField(upload_to = 'about', verbose_name = 'Arkaplan Resmi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Olusturulma Tarihi')
    
    class Meta:
        verbose_name_plural = 'Hakkımızda'
        
    def __str__(self):
        return self.title
    
class Mission(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Görevler Başlığı')
    description = RichTextField(verbose_name = 'Açıklama')
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
        verbose_name_plural = 'İletişim'
        
        
class Galery(models.Model):
    title = models.CharField(max_length = 300, verbose_name = 'Başlık')
    image = models.ImageField(upload_to='images/', verbose_name='Resim')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Galeri'
        
        
class SEOModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama", help_text="İçeriğin kısa açıklaması (SEO ve Sosyal Medya için)")
    keywords = models.CharField(max_length=300, verbose_name="Anahtar Kelimeler", blank=True, help_text="SEO için anahtar kelimeleri virgülle ayırarak girin.")
    image = models.ImageField(upload_to="seo_images/", verbose_name="Görsel", blank=True, null=True, help_text="Sosyal medyada gösterilecek görsel.")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    twitter_handle = models.CharField(max_length=100, verbose_name="Twitter Kullanıcı Adı", blank=True, null=True, help_text="Twitter kartları için kullanılır.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")    
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    
    class Meta:
        verbose_name = "SEO ve Sosyal Medya"
        verbose_name_plural = "SEO ve Sosyal Medya"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("seo_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title