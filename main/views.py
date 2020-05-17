from django.shortcuts import render, redirect
from .models import UserDetails, Exercise, Workouts
from .forms import UserForm, ExerciseForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError


# Create your views here.


def home_view(request):
    #Home page
    #Displays list of users
    # TODO: Replace this screen with a login page

    userList = UserDetails.objects.all() #sends the list of all users to the template

    #Sign up
    if (request.method=="POST" and 'signup' in request.POST):
        addUserform = UserForm(request.POST) #Form to add new user
        if addUserform.is_valid():
            #if form is valid, save the user into the dataase
            if userList.filter(user_name=request.POST['user_name']).exists():
                #userName already present
                raise ValidationError(('Username already exists'), code='invalid')
            else:
                addUserform.save()
    if (request.method=="POST" and 'login' in request.POST):
        uName = request.POST['user_name']
        pWord = request.POST['password']
        addUserform = UserForm(request.POST)
        print(uName, pWord)
        if addUserform.is_valid():
            print("Valid")
            if userList.filter(user_name=uName).exists() and userList.filter(password=pWord):
                print("user present")
                userObj = UserDetails.objects.get(user_name = uName)
                return user_home_view(request, userObj.id)
    else:
        addUserform = UserForm() #Re-render an empty form

    context = {"uList":userList, "addUserform": addUserform}
    return render(request, 'home.html', context)




    # elif (request.method == 'POST' and 'Sign in' in request.POST):
    #     uName = request.POST['user_name']
    #     pWord = request.POST['password']
    #     print(uName, pWord)
    #     return render(request, 'userhome.html',{})
    # else:
    #     return render(request, 'home.html', {})



def user_home_view(request, id):
    #Displays a list of exercise that belong to the user's workout

    #Get user_id
    #Query the database to retreive all the exercises
    # TODO: Query to get exercises specific to the user (user will be able to add exercises)
    #Pass that query as the context to populate the list of exercises the user has

    user = UserDetails.objects.get(id = id) #user
    eList = Exercise.objects.all() #exercises
    context = {"eList":eList}
    return render(request, 'userhome.html', context)

def user_exercise_view(request, ex_name):

    #Displays details about a specific exercise that belongs to a user's workout
    #Details include = User's personal best (Max weight), and a graph that plots volume vs date
    # TODO: Display grpahs


    user = UserDetails.objects.get(id = id) #user
    exercises = Exercise.objects.get(exercise_name = ex_name) #specific exercise object (benchpress, deadlift etc)

    #Form fields = ['sets', 'reps', 'weight', 'volume', 'user', 'exercise', 'date']
    #Form fields displayed to the user = ['sets', 'reps', 'weight', 'volume', 'date']
    #Model fields = ['sets', 'reps', 'weight', 'volume', 'user', 'exercise', 'date']
    if (request.method=="POST" and ("addWorkout" in request.POST)):
        #User entering data
        exerciseInput = ExerciseForm(request.POST)
        if exerciseInput.is_valid():
            # TODO: Override this method to perform more validations

            ex_form = exerciseInput.save(commit=False) #get form object before saving

            #gets sets, reps, weight and calculates volume
            ex_sets = int(request.POST['sets'])
            ex_reps =  int(request.POST['reps'])
            ex_weight = int(request.POST['weight'])
            ex_volume = ex_sets*ex_reps*ex_weight

            ex_form.volume = ex_volume #changes form's volume from default to calculatedVolume
            ex_form.user = user
            ex_form.exercise = exercises
            ex_form.save() #saves form

    else:
        #if the form is being rendered for first time => user is NOT entering form data
        #initialise form with 'user' and 'exercise' => user should NOT be able to make changes to these fields
        pre_filled = {'user': user, 'exercise': exercises}
        exerciseInput = ExerciseForm(initial = pre_filled)


    prev_workouts = Workouts.objects.filter(user=id).filter(exercise = exercises.id)
     #List of previous workouts
    p = []
    for i in prev_workouts:
        p.append([i.date, i.volume])


    context = {"ex_Form": exerciseInput, "prev_workouts":p, "ex_name":ex_name, "user":user}
    return render(request, 'userExerciseDetail.html', context)

def user_exercise_delete_view(request, id, ex_name):
    user = UserDetails.objects.get(id = id);
    exercises = Exercise.objects.get(exercise_name = ex_name)
    workouts = Workouts.objects.filter(user=id).filter(exercise = exercises.id)

    if (request.method=='POST' and 'deleteWorkout' in request.POST):
        print(request.POST, id, ex_name)
    context = {"workouts": workouts}
    return render(request, 'list_delete.html', context)

def user_exercise_delete_confirmation_view(request, id, ex_name, ex_id):
    user = UserDetails.objects.get(id = id);
    exercises = Exercise.objects.get(exercise_name = ex_name)
    workouts = Workouts.objects.filter(user=id).filter(exercise = exercises.id).filter(id = ex_id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
