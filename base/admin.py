from django.contrib import admin
from .models import (
    GeneralItem, HomeSlider,
    Phone, IslamicConditions, 
    About, Mission, 
    SubMission, Subscribe,
    PageBanner, Contact,
    Galery, MetaTag
)

@admin.register(GeneralItem)
class GeneralItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'address', 'main_phone_number', 'navbar_img', 'footer_img',)
    search_fields = ('title', 'description',)

    
@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('source', 'image')
    

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number',)
    search_fields = ('title', 'phone_number',)
    
   
@admin.register(IslamicConditions)
class IslamicConditionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon',)
    search_fields = ('title', 'description',)
   
 
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title', 'description')
    
    
class SubMissionInline(admin.TabularInline):
    model = SubMission
    extra = 1
    
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title', 'description')
    inlines = [SubMissionInline]

    
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
    
   
@admin.register(PageBanner)
class PageBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_reply', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    

@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)


@admin.register(MetaTag)
class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'name', 'content')
    list_filter = ('page_name', 'name')
    search_fields = ('page_name', 'name', 'content')