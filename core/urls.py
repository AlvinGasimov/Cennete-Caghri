from cgitb import handler
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from base.views import error

handler = error

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('base.urls', namespace='base')),
    path('makale/', include('article.urls', namespace='article')),
    path('ders/', include('lesson.urls', namespace='lesson')),
    path('galeri/', include('galery.urls', namespace='galery')),
    path('iletisim/', include('contact.urls', namespace='contact')),
    path('rosetta/', include('rosetta.urls')),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)