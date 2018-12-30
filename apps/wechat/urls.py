from django.conf.urls import include, url
from .views import WeChat

urlpatterns = [
  url(r'^$', WeChat.as_view()),
]