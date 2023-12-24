from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.core import validators
class RegiseterForm(UserCreationForm):
    username = forms.CharField(help_text='Total length must be 70 charaters', required=False,label='User name : ')
    first_name = forms.CharField(help_text='Total length must be 50 charaters')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        