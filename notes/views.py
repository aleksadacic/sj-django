from django.shortcuts import render, redirect
from .models import Notes
from django.contrib.auth.decorators import login_required
from . import forms


def notes_list(request):
    notes = Notes.objects.all().order_by('date')
    return render(request, "notes/notes_list.html", {'notes': notes})


# def note_details(request, slug):
#     # return HttpResponse(slug)
#     note = Notes.objects.get()
#     return render(request, 'notes/baza_details.html', {'notes': note})


# @login_required(login_url="/accounts/login")
# def article_create(request):
#     # if request.method == 'POST':
#     # form = forms.CreateArticle(request.POST, request.FILES)
#     # if form.is_valid():
#     #     instance = form.save(commit=False)
#     #     instance.author = request.user
#     #     instance.save()
#     #     return redirect('articles:list')
#     # else:
#     form = forms.CreateNote()
#     return render(request, 'notes/notes_create.html', {'form': form})
