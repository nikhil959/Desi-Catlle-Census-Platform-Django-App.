from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import commit
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
from betterforms.multiform import MultiModelForm
from pages.models import Post12,Imageupload1,upload

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username', 'email', 'password1','password2'] 
    class Meta:
        model=User
        fields={'username','email','password1','password2'}
        
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None,
            }   
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.username =self.cleaned_data['username']
        user.email=self.cleaned_data['email']
        
        if commit:
            user.save()
            
        return user
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)



mychoices = [
    ('camels','camels'),
    ('buffalos','buffalos'),
    ('goats','goats'),
    ('sheep','sheep'),
    ('donkeys','donkeys'),
    ('cows','cows'),
    ('chickens','chickens'),
            ] 
class uploadform(forms.ModelForm):
    
      breedname=forms.CharField(required=False)
      counts=forms.CharField(required=False)
      ownername=forms.CharField(required=False)
      email=forms.EmailField(required=False)
      aadharcard=forms.CharField(required=False)
      phonenumber=forms.CharField(required=False)
      location=forms.CharField(required=False)
      animaltype=forms.ChoiceField(choices = mychoices)
      img1=forms.ImageField(label='image upload',required=False)
      class Meta:
        model=upload
        fields=('breedname','counts','ownername','email','aadharcard','phonenumber','location','animaltype','img1')
        labels = {
               'img1': 'Please upload the Image',
             }
    

      



       
        
        
