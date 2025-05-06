from django import forms
from .models import Profiles


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['full_name', 'address_line1', 'address_line2', 'city', 'postcode', 'country', 'phone_number', 'date_of_birth', 'profile_picture']