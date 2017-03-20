from django.conf.urls import url
from .views import ResumeView, ProfileView

urlpatterns = [
    url(r'^resume/$', ResumeView.as_view(), name='resume'),
    url(r'^profile/$', ProfileView.as_view(), name='profile')
]
