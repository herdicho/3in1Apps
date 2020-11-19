from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name="dashboard"),
    path('budget/', include('budget.urls')),
    path('notes/', include('notes.urls')),
]
