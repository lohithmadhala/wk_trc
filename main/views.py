from django.shortcuts import render
from .models import User, Exercise, Workouts
from .forms import UserForm, WorkoutsForm

# Create your views here.
def home_view(request):
    #Display userlist
    #Test Data

    userList = User.objects.all()

    addUserform = UserForm()
    if (request.method=="POST"):
        print (request.POST)
        addUserform = UserForm(request.POST)
        if addUserform.is_valid():
            addUserform.save()


    context = {"uList":userList, "addUserform": addUserform}
    return render(request, 'home.html', context)

def user_home_view(request, id):
    #Get user_name or user_id
    #Query the databases
    #Pass that query as the context to populate the list of exercises the user has
    eList = ['DeadLift', 'Squat', 'Benchpress', 'Pullup', 'Overheadpress', 'BentOverRows']
    user = User.objects.get(id = id)
    #eList = Workouts.objects.filter(user = user)

    addExerciseForm = WorkoutsForm()
    if (request.method == "POST"):
        print(request.POST)
        addExerciseForm = WorkoutsForm(request.POST)
        if addExerciseForm.is_valid():
            addExerciseForm.save()

    context = {"eList":eList, "addExerciseForm": addExerciseForm}
    return render(request, 'userhome.html', context)

def user_exercise_view(request):
    return render(request, 'userExerciseDetail.html', {})
