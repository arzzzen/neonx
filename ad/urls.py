from django.conf.urls import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
    patterns('ad.views',
    (r'^$', 'home'),
    (r'^registration', 'registration'),
    (r'^archive', 'archive'),
    (r'^addition', 'addition'),
    (r'^login', 'login_user'),
    (r'^logout', 'userlogout'),
    (r'^(?P<urlcity>[a-z-]+)$','cityarchive'),
    (r'^(?P<urlcity>[a-z-]+)/(?P<urlcategory>[a-z-]+)','categoryarchive'),
)
