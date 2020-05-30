# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from apps.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
