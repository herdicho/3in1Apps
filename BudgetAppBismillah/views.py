from django.shortcuts import render, redirect

def dashboard(request):
   
    return render(request, 'main_dashboard.html')