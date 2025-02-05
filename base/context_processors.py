from .models import (
    GeneralItem, HomeSlider, 
    Phone, IslamicConditions,
    About, Mission, PageBanner,
    MetaTag
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
    page_slug = request.path.strip("/").split("/")[0]
    
    if not page_slug:
        page_slug = "none"
    
    meta_tags = MetaTag.objects.filter(slug=page_slug)
    og_tags = [tag for tag in meta_tags if tag.name.startswith("og:")]
    twitter_tags = [tag for tag in meta_tags if tag.name.startswith("twitter:")]
    other_tags = [tag for tag in meta_tags if not tag.name.startswith(("og:", "twitter:"))]
    
    context = {
        'item' : item,
        'phones' : phones,
        'conditions' : islamic_conditions,
        'about' : about,
        'mission' : mission,
        'last_6_articles' : last_6_articles,
        'home_sliders' : home_sliders,
        'banner' : banner,
        'og_tags': og_tags,
        'twitter_tags': twitter_tags,
        'other_tags': other_tags,
    }
    
    return context