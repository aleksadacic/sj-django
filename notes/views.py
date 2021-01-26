import sys

from django.shortcuts import render, redirect
from .models import Notes
from . import forms
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login")
def notes_list(request):
    notes = Notes.objects.filter(user_id=request.user.id).order_by('-date')
    form = forms.CreateNote()
    update_form = forms.UpdateNote()
    return render(request, "notes/notes_list.html", {'notes': notes, 'form': form, 'update_form': update_form})


@login_required(login_url="/accounts/login")
def notes_create(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('notes:list')
    else:
        form = forms.CreateNote()
    notes = Notes.objects.filter(user_id=request.user.id).order_by('-date')
    return render(request, 'notes/notes_list.html', {'notes': notes, 'form': form})


@login_required(login_url="/accounts/login")
def notes_delete(request):
    note_id = request.POST.get('id_note')
    if request.method == 'POST':
        note = Notes.objects.get(pk=note_id)
        if note.user == request.user.id:
            note.delete()
    return redirect('notes:list')


@login_required(login_url="/accounts/login")
def notes_search(request):
    notes = Notes.objects.filter(user_id=request.user.id).order_by('-date')
    if request.method == 'POST':
        query = request.POST.get('query')
        if len(query) > 0:
            notes = Notes.objects.filter(text__contains=query, user_id=request.user.id).order_by('-date')
    form = forms.CreateNote()
    update_form = forms.UpdateNote()
    return render(request, 'notes/notes_list.html', {'notes': notes, 'form': form, 'update_form': update_form})

@login_required(login_url="/accounts/login")
def notes_update(request):
    if request.method == 'POST':
        update_form = forms.UpdateNote(request.POST, request.FILES)
        if update_form.is_valid():
            note_id = request.POST.get('id_note')
            note = Notes.objects.get(pk=note_id)
            if note.user == request.user.id:
                note.text = update_form['text'].value()
                note.save()
    return redirect("notes:list")
