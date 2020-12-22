from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('notes/', include("notes.urls")),
    path('todos/', include("todos.urls")),
    path('accounts/', include("accounts.urls")),

]
