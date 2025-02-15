from django.shortcuts import render, redirect
from .models import Paciente
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.
def index(request):
  queixas = Paciente.queixa_choices
  if request.method == "GET":
    return render(request, 'index.html', {'queixas': queixas})
  elif request.method == "POST":
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    queixa = request.POST.get('queixa')
    foto = request.FILES.get('foto')
    if len(nome.strip()) or not foto:
      messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
      return redirect('index')
    paciente = Paciente(
      nome=nome,
      email=email,
      telefone=telefone,
      queixa=queixa,
      foto=foto)
    paciente.save()
    messages.add_message(request, constants.SUCCESS, 'Paciente salvo com sucesso!')
    return redirect('index')