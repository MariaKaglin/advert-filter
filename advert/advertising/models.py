from django.db import models
from django import forms
# Create your models here.

class Function(forms.Form):
    file_path = forms.FileField()
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()

class hands_param(forms.Form):
    y_0 = forms.IntegerField()
    x_0 = forms.IntegerField()
    beta = forms.IntegerField()
    T = forms.IntegerField()

class auto_param(forms.Form):
    y_0 = forms.IntegerField()
    beta_from = forms.IntegerField()
    beta_to = forms.IntegerField()
    T = forms.IntegerField()
    
class auto(forms.Form):
    auto_ = forms.BooleanField()
