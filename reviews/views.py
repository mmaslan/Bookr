from django.shortcuts import render


def index(request):
    name = "świecie"
    return render(request, "base.html", {'name': invalid_name})
