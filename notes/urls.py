from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name="list"),
    path('create/', views.notes_create, name="create"),
    path('delete/', views.notes_delete, name="delete"),
    path('search/', views.notes_search, name="search"),
    path('update/', views.notes_update, name="update"),
    # url(r'^(?P<>[\w-]+)/$', views.note_details, name="details")
]
