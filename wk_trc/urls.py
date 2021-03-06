"""wk_trc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import home_view, user_home_view, user_exercise_view, user_exercise_delete_view,user_exercise_delete_confirmation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="userList"),
    path('<int:id>/', user_home_view, name="userExerciseList"), #take user_name here <string>
    path('<int:id>/<slug:ex_name>/', user_exercise_view, name="userExerciseDetail"),
    path('<int:id>/<slug:ex_name>/delete/', user_exercise_delete_view, name='userExerciseDelete'),
    path('<int:id>/<slug:ex_name>/delete/<int:ex_id>', user_exercise_delete_confirmation_view, name='userExerciseDeleteConfirm')

]
