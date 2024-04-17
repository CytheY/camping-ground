from django import forms
from .models import Campground
 
 
class CampgroundForm(forms.ModelForm):
 
    class Meta:
        model = Campground
        fields = ['name', 'campground_image']