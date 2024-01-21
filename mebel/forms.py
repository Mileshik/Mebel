from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('published_date','user','comments')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SingUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
