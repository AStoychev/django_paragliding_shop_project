from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paragliding_shop.accounts.urls')),
    path('', include('paragliding_shop.equipment.urls')),
    path("unicorn/", include("django_unicorn.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
