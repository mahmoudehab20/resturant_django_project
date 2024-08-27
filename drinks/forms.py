from django import forms
from .models import drinks

class DrinksModelForm(forms.ModelForm):
    class Meta:
        model=drinks
        fields='__all__'