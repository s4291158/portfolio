from django.conf.urls import url
from .views import ResumeView
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='resume'), name='index'),
    url(r'^resume/$', ResumeView.as_view(), name='resume')
]
