from . import models
from django import forms

# Create your models here.
class studentForm(forms.ModelForm):
    class Meta:
        model=models.student
        fields=['name','mobile','email','message']
        widgets = {
            "name": forms.TextInput(attrs={"class": "formfield",'placeholder': 'Name*'}),
            "mobile": forms.TextInput(attrs={"class": "formfield",'placeholder': 'Mobile*'}),
            "email": forms.TextInput(attrs={"class": "formfield",'placeholder': 'Email*'}),
            "message": forms.TextInput(attrs={"class": "formfield",'placeholder': 'Message*'}),
            
        }