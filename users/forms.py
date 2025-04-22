from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'avatar', 'phone_number', 'country']
