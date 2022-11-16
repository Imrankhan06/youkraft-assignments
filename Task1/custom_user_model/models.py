from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password


# Create your models here.
class UserModel(models.Model):
    """ Creating custom user model fields """
    username = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)


@receiver(pre_save, sender=UserModel)
def create_user(sender, instance, **kwargs):
    """ Using signals pre_save to hash the password """

    instance.password = make_password(instance.password)


pre_save.connect(create_user, sender=UserModel)
