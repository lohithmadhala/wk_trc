from django.forms import ModelForm
from .models import UserDetails, Exercise, Workouts
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'

class ExerciseForm(ModelForm):
    class Meta:
        model = Workouts

        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'exercise': forms.HiddenInput(),
            'volume': forms.HiddenInput(),
        }
