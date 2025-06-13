from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),        # Home, about, etc.
    path('pages/', include('pages.urls')), # Páginas del blog
    path('accounts/', include('accounts.urls')),  # Login, perfil, etc.
    path('messages/', include('messaging.urls')),

]

# Servir archivos media (como avatares) en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
