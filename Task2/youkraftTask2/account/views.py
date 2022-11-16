from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from . import forms


@csrf_exempt
def authenticate(request):
    """
    Get the username and password from form and validate the password from DB
    """
    form = forms.AuthenticateForm()
    if request.method == "POST":
        form = forms.AuthenticateForm(request.POST)
        username = request.POST['username']
        entered_password = request.POST['password']
        if form.is_valid():
            query = User.objects.filter(username=username).values('password')
            saved_password = query[0]['password']
            if entered_password != saved_password:
                message = {'message': "Passwords do not match", 'status': status.HTTP_403_FORBIDDEN}
                return render(request, 'registration/login.html', context={'form': form, 'message': message})
            else:
                context = {
                    'message': "Passwords match",
                    'status': status.HTTP_200_OK
                }
                return JsonResponse(context)

    return render(request, 'registration/login.html', context={'form': form})


@csrf_exempt
def register(request):
    """ Creating a new user and validate the username already exists in db """
    message = ""
    if request.method == "POST":
        form = forms.AddUserForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = request.POST['username']
            user.password = request.POST['password']
            try:
                user = User.objects.get(username=user.username)
                message = "User Name Taken!"
            except User.DoesNotExist:
                user.save()
                message = "New User Created!!"
        else:
            form = forms.AddUserForm(request.POST)
            message = "User cannot be created."
            return render(request, 'registration/register.html', context={'form': form, 'message': message})
    else:
        form = forms.AddUserForm()
    return render(request, 'registration/register.html', context={'form': form, 'message': message})
