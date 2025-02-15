from django.shortcuts import render
from .models import Paciente
# Create your views here.
def index(request):
  queixas = Paciente.queixa_choices
  return render(request, 'index.html', {'queixas': queixas})