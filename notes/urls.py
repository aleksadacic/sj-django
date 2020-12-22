from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name="list"),
    # path('create/', views.notes_create, name="create"),
    # url(r'^(?P<>[\w-]+)/$', views.note_details, name="details")
]
