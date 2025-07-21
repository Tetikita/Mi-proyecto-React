from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola, mundo!")

urlpatterns = [
    path('', home, name='home'),
]
