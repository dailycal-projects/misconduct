from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

urlpatterns = [
    url(r'^misconduct/', include('misconduct.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)