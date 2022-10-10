from django.shortcuts import render

def welcome_view(request):
    return render(request, 'base.html')