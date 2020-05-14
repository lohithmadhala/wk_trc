from django.forms import ModelForm
from .models import User, Exercise, Workouts

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
