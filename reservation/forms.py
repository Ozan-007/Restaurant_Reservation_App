from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Table
#Forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']



class TableForm(forms.ModelForm):
    class meta:
        model = Table
        fields = "__all__"