from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^certificate/(?P<email>[\s\S]*)$', views.certificate)
]

