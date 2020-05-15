from django.shortcuts import render
from .models import User, Exercise, Workouts
from .forms import UserForm, ExerciseForm

# Create your views here.
def home_view(request):
    #Display userlist
    #Test Data

    userList = User.objects.all()

    addUserform = UserForm()
    if (request.method=="POST"):
        # print (request.POST)
        addUserform = UserForm(request.POST)
        print(addUserform.is_valid())
        if addUserform.is_valid():
            addUserform.save()

    context = {"uList":userList, "addUserform": addUserform}
    return render(request, 'home.html', context)

def user_home_view(request, id):
    #Get user_name or user_id
    #Query the databases
    #Pass that query as the context to populate the list of exercises the user has
    #eList = ['DeadLift', 'Squat', 'Benchpress', 'Pullup', 'Overheadpress', 'BentOverRows']
    user = User.objects.get(id = id)
    eList = Exercise.objects.all()
    print(eList)

    context = {"eList":eList}
    return render(request, 'userhome.html', context)

def user_exercise_view(request, id, ex_name):
    user = User.objects.get(id = id)
    exercises = Exercise.objects.get(exercise_name = ex_name)

    print(request.POST)
    if (request.method=="POST"):
        pre_filled = {'user': user, 'exercise': exercises}
        exerciseInput = ExerciseForm(request.POST)
        print (exerciseInput.is_valid())

        if exerciseInput.is_valid():
            print("valid")
            exerciseInput.save()


    else:
        print("user going to enter data")
        pre_filled = {'user': user, 'exercise': exercises}
        exerciseInput = ExerciseForm(initial = pre_filled)

    prev = [100, 250, 500, 800, 1000, 1250]

    prev = Workouts.objects.filter(user=id)

    context = {"ex_Form": exerciseInput, "prev":prev, "ex_name":ex_name, "user":user}
    return render(request, 'userExerciseDetail.html', context)
