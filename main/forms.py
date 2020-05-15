from django.forms import ModelForm
from .models import User, Exercise, Workouts
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ExerciseForm(ModelForm):
    class Meta:
        model = Workouts
        # fields = [
        #     'sets',
        #     'reps',
        #     'weight',
        #     'volume',
        #     'date'
        # ]

        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'exercise': forms.HiddenInput(),
        }
