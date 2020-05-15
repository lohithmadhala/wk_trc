from django.db import models

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)

    def __str__(self):
        return(self.exercise_name)

class User(models.Model):
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return(self.user_name)

class Workouts(models.Model):
    reps = models.IntegerField(default = 0)
    sets = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    volume = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE)
    date = models.IntegerField()

    def __str__(self):
        return (self.exercise.exercise_name+" "+str(self.date)+" "+str(self.volume))
