from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ad.views import ad
from ad.views.cat import CatViewSet
from ad.views.selection import SelectionViewSet
from user.views.location import LocViewSet

router = routers.SimpleRouter()
router.register('loc', LocViewSet)
router.register('cat', CatViewSet)
router.register('selection', SelectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ad_search/', ad.AdListView.as_view()),
    path('user/', include('user.urls')),
    path('ad/', include('ad.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
