from django.shortcuts import render
from .models import UserDetails, Exercise, Workouts
from .forms import UserForm, ExerciseForm

# Create your views here.
def home_view(request):
    #Home page
    #Displays list of users
    # TODO: Replace this screen with a login page

    userList = UserDetails.objects.all() #sends the list of all users to the template


    if (request.method=="POST"):
        addUserform = UserForm(request.POST) #Form to add new user
        if addUserform.is_valid():
            #if form is valid, save the user into the dataase
            addUserform.save()

    addUserform = UserForm() #Re-render an empty form
    context = {"uList":userList, "addUserform": addUserform}
    return render(request, 'home.html', context)

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

def user_exercise_view(request, id, ex_name):

    #Displays details about a specific exercise that belongs to a user's workout
    #Details include = User's personal best (Max weight), and a graph that plots volume vs date
    # TODO: Display grpahs


    user = UserDetails.objects.get(id = id) #user
    exercises = Exercise.objects.get(exercise_name = ex_name) #specific exercise object (benchpress, deadlift etc)

    #Form fields = ['sets', 'reps', 'weight', 'volume', 'user', 'exercise', 'date']
    #Form fields displayed to the user = ['sets', 'reps', 'weight', 'volume', 'date']
    #Model fields = ['sets', 'reps', 'weight', 'volume', 'user', 'exercise', 'date']
    if (request.method=="POST"):
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


    prev_workouts = Workouts.objects.filter(user=id).filter(exercise = exercises.id) #List of previous workouts


    context = {"ex_Form": exerciseInput, "prev_workouts":prev_workouts, "ex_name":ex_name, "user":user}
    return render(request, 'userExerciseDetail.html', context)
