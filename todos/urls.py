from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_list, name="list"),
    path('create/', views.todos_create, name="create"),
    path('delete/<int:todo_id>/', views.todos_delete, name="delete"),

]
