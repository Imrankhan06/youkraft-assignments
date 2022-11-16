from django import forms


class AuthenticateForm(forms.Form):
    """ Form fields to authenticate username and password """
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)


class AddUserForm(forms.Form):
    """ Form fields to create a new user """
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
