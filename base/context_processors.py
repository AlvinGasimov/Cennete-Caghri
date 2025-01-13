from .models import (
    GeneralItem, HomeSlider, 
    Phone, IslamicConditions,
    About, CommunityService,
    Service, Mission, PageBanner
)
from article.models import ArticleCategory, Article

def site_settings(request):
    
    
    item = GeneralItem.objects.all().order_by('-created_at').first()
    home_sliders = HomeSlider.objects.all().order_by('-created_at').all()
    phones = Phone.objects.all().order_by('-created_at').all()
    islamic_conditions = IslamicConditions.objects.all()
    about = About.objects.all().order_by('-created_at').first()
    community_service = CommunityService.objects.all().order_by('-created_at').first()
    services = Service.objects.all().order_by('-created_at').all()
    mission = Mission.objects.all().order_by('-created_at').first()
    last_6_articles = Article.objects.all().order_by('-created_at')[:6]
    banner = PageBanner.objects.all().first()
    
    context = {
        'item' : item,
        'phones' : phones,
        'conditions' : islamic_conditions,
        'about' : about,
        'community_service' : community_service,
        'services' : services,
        'mission' : mission,
        'last_6_articles' : last_6_articles,
        'home_sliders' : home_sliders,
        'banner' : banner
    }
    
    return context