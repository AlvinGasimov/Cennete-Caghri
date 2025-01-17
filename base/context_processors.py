from .models import (
    GeneralItem, HomeSlider, 
    Phone, IslamicConditions,
    About, Mission, PageBanner, 
    SEOModel
)
from article.models import ArticleCategory, Article

def site_settings(request):
    
    
    item = GeneralItem.objects.all().order_by('-created_at').first()
    home_sliders = HomeSlider.objects.all().order_by('-created_at').all()
    phones = Phone.objects.all().order_by('-created_at').all()
    islamic_conditions = IslamicConditions.objects.all()
    about = About.objects.all().order_by('-created_at').first()
    mission = Mission.objects.all().order_by('-created_at').first()
    last_6_articles = Article.objects.all().order_by('-created_at')[:6]
    banner = PageBanner.objects.all().first()
    seo = SEOModel.objects.all().order_by('-created_at').first()
    
    context = {
        'item' : item,
        'phones' : phones,
        'conditions' : islamic_conditions,
        'about' : about,
        'mission' : mission,
        'last_6_articles' : last_6_articles,
        'home_sliders' : home_sliders,
        'banner' : banner,
        'seo' : seo
    }
    
    return context