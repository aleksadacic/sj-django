from django.shortcuts import render, redirect
from .models import Todos
from . import forms
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login")
def todo_list(request):
    todos = Todos.objects.filter(user_id=request.user.id).order_by('time')
    form = forms.CreateTodo()
    return render(request, "todos/todos_list.html", {'todos': todos, 'form': form})


@login_required(login_url="/accounts/login")
def todos_create(request):
    if request.method == 'POST':
        form = forms.CreateTodo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('todos:list')
    else:
        form = forms.CreateTodo()
    todos = Todos.objects.filter(user_id=request.user.id).order_by('time')
    return render(request, 'todos/todos_list.html', {'form': form, 'todos': todos})


@login_required(login_url="/accounts/login")
def todos_delete(request, todo_id=None):
    if request.method == 'POST':
        todo = Todos.objects.get(pk=todo_id)
        todo.delete()
    return redirect('todos:list')
