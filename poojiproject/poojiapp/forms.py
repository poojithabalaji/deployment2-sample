from django import forms
from poojiapp.models import studentdetails
from django.forms import ModelForm

class studentform(forms.ModelForm):
    class  Meta:
        model = studentdetails
        fields= ['first_name','sur_name','father_name','mother_name']
