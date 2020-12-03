from django import forms
from .models import Category, SubCategory


class UploadFileForm(forms.Form):
    file = forms.FileField()
