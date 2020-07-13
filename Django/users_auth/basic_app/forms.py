from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInto

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileIntoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInto
        fields = ('portfolio_site', 'profile_pic')
