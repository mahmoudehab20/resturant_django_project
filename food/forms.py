from django import forms
from .models import MainDish,appetizers,souces

class MainModelForm(forms.ModelForm):
    class Meta:
        model=MainDish
        fields='__all__'

class AppetizersModelForm(forms.ModelForm):
    class Meta:
        model=appetizers
        fields='__all__'

class SouceModelForm(forms.ModelForm):
    class Meta:
        model=souces
        fields='__all__'
