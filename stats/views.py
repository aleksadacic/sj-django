import sys

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from notes.models import Notes
from todos.models import Todos
from django.contrib.auth.models import User


@login_required(login_url="/accounts/login")
def stats_page(request):
    if not User.is_superuser:
        return

    labels = ['notes', 'todos']
    data = []
    avg_notes = 0
    avg_todos = 0
    avg_time = 0

    notes = Notes.objects.order_by('date')
    todos = Todos.objects.order_by('time')
    notecnt = 0
    todocnt = 0

    users = []
    times = []
    for note in notes:
        notecnt += len(note.text)
        times.append(note.date.time().hour)
        if not users.__contains__(note.user_id):
            users.append(note.user_id)

    data.append(notecnt)
    for todo in todos:
        todocnt += len(todo.text)
        times.append(todo.time.hour)
        if not users.__contains__(note.user_id):
            users.append(note.user_id)

    avg_time = int(sum(times) / len(times))
    avg_notes = notecnt/len(users)
    avg_todos = todocnt/len(users)
    data.append(todocnt)
    return render(request, 'stats/stats_page.html', {
        'labels': labels,
        'data': data,
        'avg_notes': avg_notes,
        'avg_todos': avg_todos,
        'avg_time': avg_time
    })
