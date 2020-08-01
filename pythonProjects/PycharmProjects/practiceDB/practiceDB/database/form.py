from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model=database
        fields=['student_image' , 'student_name' , 'student_class']