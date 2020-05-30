from django.forms import ModelForm
from .models import Note, Topic
from django import forms

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'notes', 'title']

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']
        