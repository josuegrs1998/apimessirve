from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .views import PasswordCheckViewSet

router = DefaultRouter()
router.register(r'revisar-contra', PasswordCheckViewSet)

urlpatterns =[
    url(r'', include(router.urls))
]