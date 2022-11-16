from rest_framework import serializers
from custom_user_model.models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    """ Serializer for custom user model """
    class Meta:
        model = UserModel
        fields = [
            'username',
            'email',
            'password'
        ]
