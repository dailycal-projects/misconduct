from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from misconduct.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', CaseListView.as_view(), name='case-list'),
    url(r'^case/(?P<slug>[-\w]+)/$', CaseDetailView.as_view(), name='case-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)