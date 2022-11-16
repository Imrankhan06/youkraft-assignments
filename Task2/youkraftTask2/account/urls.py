from django.urls import path
# from django.contrib.auth import views
from account import views

urlpatterns = [
    path('user/register/', views.register, name="register"),
    path('user/authenticate/', views.authenticate, name="authenticate"),

]
