from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import start_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_page, name='start'),
    path('users/', include('app_users.urls'), name='users'),
    path('works/', include('app_works.urls'), name='works'),
    path('i18n', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
