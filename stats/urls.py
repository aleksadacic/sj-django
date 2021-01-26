from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.stats_page, name="stats_page"),
    # path('create/', views.notes_create, name="create"),
    # url(r'^(?P<>[\w-]+)/$', views.note_details, name="details")
]
