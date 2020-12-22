from django.shortcuts import render, redirect
from .models import Todos
from . import forms


def todo_list(request):
    notes = Todos.objects.all().order_by('time')
    return render(request, "todos/todos_list.html", {'notes': notes})


# login anotacija
def todos_create(request):
    if request.method == 'POST':
        form = forms.CreateTodo(request.POST, request.FILES)
        # if form.is_valid():
        # PRVO IDE LOGIN
        # instance = form.save(commit=False)
        # instance.author = request.user
        # instance.save()
        # return redirect('notes:list')
    else:
        form = forms.CreateTodo()
    return render(request, 'todos/todos_create.html', {'form': form})
