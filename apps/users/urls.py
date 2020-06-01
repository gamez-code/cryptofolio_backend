# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from django.urls import path
from apps.users.views import UserViewSet, CreateUser

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
