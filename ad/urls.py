from django.conf.urls.defaults import *

urlpatterns = patterns('ad.views',
    (r'^$', 'home'),
    (r'^registration', 'registration'),
    (r'^archive', 'archive'),
    (r'^addition', 'addition'),
    (r'^logout', 'userlogout'),
    (r'^(?P<urlcity>[a-z-]+)$','cityarchive'),
    (r'^(?P<urlcity>[a-z-]+)/(?P<urlcategory>[a-z-]+)','categoryarchive'),
)