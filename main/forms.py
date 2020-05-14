from django.forms import ModelForm
from .models import User, Exercise, Workouts

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class WorkoutsForm(ModelForm):
    class Meta:
        model = Workouts
        fields = [
            'reps',
            'sets',
            'weight',
            'volume',
            'exercise',
            'date'
        ]
