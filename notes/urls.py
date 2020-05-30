from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_notes"),
    path('create_note/<str:pk>/', views.createNote, name="create_note"),
    path('delete_note/<str:pk>/', views.deleteNote, name="delete_note"),
    path('update_note/<str:pk>/', views.updateNote, name="update_note"),
    path('create_topic/', views.createTopic, name="create_topic"),

    path('update_clear_status/<str:pk>/', views.updateClearStatus, name="update_clear_status"),
   ]