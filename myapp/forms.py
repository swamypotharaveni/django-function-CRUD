from django import forms
from myapp.models import shop1

class shopform(forms.ModelForm):
    class Meta:
        model=shop1
        fields='__all__'