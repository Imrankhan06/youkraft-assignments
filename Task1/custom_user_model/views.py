from django.shortcuts import render
from rest_framework import viewsets

from custom_user_model.serializers import UserModelSerializer
from custom_user_model.models import UserModel


# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    """ Using ModelViewSet to perform CURD operations """
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
