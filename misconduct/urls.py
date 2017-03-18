from misconduct.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', CaseListView.as_view(), name='case-list'),
    url(r'^case/(?P<slug>[-\w]+)/$', CaseDetailView.as_view(), name='case-detail'),
    url(r'^stories/$', StoryView.as_view(), name='stories'),
    url(r'^about/$', AboutView.as_view(), name='about'),
]