from django.shortcuts import render, redirect
from .models import Notes
from . import forms


def notes_list(request):
    notes = Notes.objects.all().order_by('date')
    return render(request, "notes/notes_list.html", {'notes': notes})

#login anotacija
def notes_create(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        # if form.is_valid():
            # PRVO IDE LOGIN
            # instance = form.save(commit=False)
            # instance.author = request.user
            # instance.save()
            # return redirect('notes:list')
    else:
        form = forms.CreateNote()
    return render(request, 'notes/notes_create.html', {'form': form})
