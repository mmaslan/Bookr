from django.http import HttpResponse
from models import Book


def welcome_view(request):
    message = f"<html><h1>Witaj w witrynie Bookr!</h1>"\
        "<p>{Book.objects.count()} książek i stale dodajemy nowe!</p></html>"
    return HttpResponse(message)