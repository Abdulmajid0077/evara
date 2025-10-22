from django import forms
import re
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form__input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form__input"}))

    def clean_username(self):
        value = self.cleaned_data['username']

        if re.fullmatch(r"[A-Za-z0-9]{8}", value) is None:
            raise forms.ValidationError("username 8 honali va katta kichik harflar va raqamlardan bo'lsin")
        
        return value
    
    def clean_password(self):
        value = self.cleaned_data['password']

        if re.fullmatch(r"[A-Za-z0-9]{8}", value) is None:
            raise forms.ValidationError("password 8 honali va katta kichik harflar va raqamlardan bo'lsin")
        
        return value
    
class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form__input", "placeholder":"First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form__input", "placeholder":"Last name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form__input", "placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form__input", "placeholder":"Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form__input", "placeholder":"Password"}))
    reset_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form__input", "placeholder":"Reset Password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username is None:
            raise forms.ValidationError('Username kiritilishi kerak')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu nom allaqachon mavjud')
        
        return username
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email is None:
            raise forms.ValidationError('Email kiritilishi kerak')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email allaqachon mavjud')
        
        return email
        
    def clean_reset_password(self):
        password = self.cleaned_data.get('password')
        reset_password = self.cleaned_data.get('reset_password')

        if password != reset_password:
            raise forms.ValidationError('Passwordlar birxil bolishi kerak')
        
        return password