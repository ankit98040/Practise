from django import forms
from .models import *
#from django.forms import ModelForm

class Add_Album_Form(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ()
        ####html widgets
        widgets = {
            "name":forms.TextInput(attrs={"class":"Input", "placeholder":"Album Name From Forms"}),
            "artist":forms.TextInput(attrs={"class":"Input", "placeholder":"Album Artist Name"}),
            "image":forms.FileInput(attrs={"class":"Input"}),
        }