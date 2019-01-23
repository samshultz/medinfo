from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, MedicalInfo


class UserRegistrationForm(UserCreationForm):    

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'is_doctor']
        

class MedicalInfoForm(forms.ModelForm):
    class Meta:
        model = MedicalInfo
        exclude = 'patient',