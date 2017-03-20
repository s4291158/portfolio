from django.conf.urls import url
from .views import ResumeView

urlpatterns = [
    url(r'^resume/$', ResumeView.as_view(), name='resume')
]
