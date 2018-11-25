from django import forms
from .models import UserStatus,Neighborhood,Business,Post,Health

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['writer']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserStatus
        exclude = ['user']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = UserStatus
        exclude = ['user','user_image','user_email']
