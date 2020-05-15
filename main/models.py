from django.db import models

class Exercise(models.Model):
    #Exercise table -> exercise name, id
    exercise_name = models.CharField(max_length=100)

    def __str__(self):
        return(self.exercise_name)

class UserDetails(models.Model):
    #UserDetails table -> user_name, id
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return(self.user_name)

class Workouts(models.Model):
    #Workouts table -> reps, sets, weight, volume, user (ForeignKey: one user can have many workouts), exercise (ForeignKey: one workout can have many exercise),
    #volume (calculated by sets*reps*weight), and date

    reps = models.IntegerField()
    sets = models.IntegerField()
    weight = models.IntegerField()
    volume = models.IntegerField(default = 0)
    user = models.ForeignKey(UserDetails, on_delete = models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE)
    date = models.IntegerField()

    def __str__(self):
        return (self.exercise.exercise_name+" "+str(self.date)+" "+str(self.volume))
