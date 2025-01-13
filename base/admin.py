from django.contrib import admin
from .models import (
    GeneralItem, HomeSlider,
    Phone, IslamicConditions, 
    About, CommunityService, 
    Service, Mission, 
    SubMission, Subscribe,
    PageBanner
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
    
    
    
@admin.register(CommunityService)
class CommunityServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title', 'description')
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon',)
    search_fields = ('title', 'description',)
    
    
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