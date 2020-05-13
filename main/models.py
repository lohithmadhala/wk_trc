from django.db import models

class Exercise(models.Model):
    ex_name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()
    volume = models.IntegerField(default = 1000)

class Workout(models.Model):
    date = models.IntegerField()
    # exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE, null = True)
    wk_id = models.IntegerField()

class Users(models.Model):
    u_name = models.CharField(max_length=100)
    # workout = models.ForeignKey(Workout, on_delete = models.CASCADE, null = True)
