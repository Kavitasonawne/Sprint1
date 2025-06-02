from django import forms
from django.contrib.auth.models import User
from .models import Complaint
from django.contrib.auth.forms import UserCreationForm

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'person_name',       # 1st
            'contact_number',    # 2nd
            'title',            # 3rd
            'description',      # 4th
            'gender',           # 5th
            'category',         # 6th
            'area',             # 7th
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'person_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter your contact number'}),
            'area': forms.TextInput(attrs={'placeholder': 'Enter your street or area'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']