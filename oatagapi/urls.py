
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bio.views import biolink


# Serializers define the API representation.


urlpatterns = [
    path('<str:page_alias>', biolink, name='biolink'),
    path('admin/', admin.site.urls),
    path('auth/', include('account.urls') , name='auth_urls'),
    path('bio/', include('bio.urls') , name='bio_urls'),
    path('qr/', include('qrapp.urls') , name='qr_urls'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)