from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':"field",  "placeholder":'Username'}))
    email=forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':"field", "placeholder":'Email'}))
    password1=forms.CharField(min_length=8 ,max_length=255, required=True, widget=forms.PasswordInput(attrs={'class':"field",  "placeholder":'Password'}))
    password2=forms.CharField(min_length=8 ,max_length=255, required=True, widget=forms.PasswordInput(attrs={'class':"field",  "placeholder":'Confirm Password'}))
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    bio=forms.CharField(required=True, widget=forms.Textarea(attrs={'class':"field", "placeholder":'Bio'}))
    birthday=forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'class':"field",  "placeholder":'Birthday'}))
    location=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"field",  "placeholder":'Location'}))
    class Meta:
        model=Profile
        fields=('avatar', 'bio', 'birthday', 'location')
