from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def sayandip(request):
    return HttpResponse("Hello, Sayandip!")


def greet(request, name: str):
    return render(request, "hello/greet.html", {
               "name": name.capitalize()
           })
