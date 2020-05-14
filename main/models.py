from django.db import models

class Exercise(models.Model):
    CHOICES =(
        ('DeadLift', 'DeadLift'),
        ('Rows', 'Rows'),
        ('Benchpress', 'Benchpress'),
        ('Squat', 'Squat'),
        ('Overheadpress', 'Overheadpress'),
        ('Pullup', "Pullup")
    )
    exercise_name = models.CharField(max_length=100, choices = CHOICES)

class User(models.Model):
    user_name = models.CharField(max_length=100)

class Workouts(models.Model):
    reps = models.IntegerField(default = 0)
    sets = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    volume = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE)
    date = models.IntegerField()
