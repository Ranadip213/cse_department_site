from django import forms
from django.forms import ModelForm
from .models import contactus

class contactuoform(ModelForm):
    class Meta:
        model = contactus
        fields = '__all__'
