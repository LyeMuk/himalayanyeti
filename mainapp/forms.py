from django import forms
from . models import article, label, categories

from django.forms import inlineformset_factory

class articleform(forms.ModelForm):
    class Meta:
        model=article
        fields="__all__"


