from django.urls import include, path

from rest_framework import routers

from custom_user_model.views import UserModelViewSet

router = routers.DefaultRouter()
router.register(r'users', UserModelViewSet)

urlpatterns = [
   path('', include(router.urls)),
]