from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import NoteForm, TopicForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse

def home(request):
   last5Notes = Note.objects.all().order_by('-date_created')[:5]
   topics = Topic.objects.all()
   #notes = Note.objects.all().order_by('-date_created')
   notes = Note.objects.all().order_by('clear')

   # paginator topic
   paginator = Paginator(topics, 5)
   page = request.GET.get('page')
   try:
      topicsPage = paginator.page(page)
   except PageNotAnInteger:
      topicsPage = paginator.page(1)
   except EmptyPage:
      topicsPage = paginator.page(paginator.num_pages)

   context = {
      'last5Notes' : last5Notes,
      'notes' : notes,
      'topicsPage' : topicsPage
   }
   
   return render(request, 'notes/dashboard.html', context)


def createNote(request, pk):
   topic = Topic.objects.get(id=pk)

   form = NoteForm(initial={'topic':topic})
   form.fields['topic'].widget.attrs['readonly'] = True
   if request.method == 'POST':
      form = NoteForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/notes')

   context = {
      'form':form
   }

   return render(request, 'notes/create_new_notes.html', context)


def deleteNote(request, pk):
   Note.objects.filter(id=pk).delete()
   return redirect('/notes')


def updateNote(request, pk):
   note = Note.objects.get(id=pk)
   form = NoteForm(instance=note)

   if request.method == 'POST':
      form = NoteForm(request.POST, instance=note)
      if form.is_valid():
         form.save()
         return redirect('/notes')

   context = {
      'form':form
   }

   return render(request, 'notes/update_notes.html', context)


def createTopic(request):
   form = TopicForm()
   if request.method == 'POST':
      form = TopicForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/notes')

   context = {
      'form':form
   }

   return render(request, 'notes/create_new_topic.html', context)


def updateClearStatus (request, pk):
   note = Note.objects.get(id=pk)
   note.clear = not note.clear
   note.save()
   return redirect('/notes') 
