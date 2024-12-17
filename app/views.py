from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages import constants as messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


def homepage(request):
    return render(request, 'app/homepage.html')

def fazer_login(request):
    return render(request, 'app/login.html')

def criar_conta(request):
    return render(request, 'app/criar_conta.html')

def perfil(request):
    return render(request, 'app/perfil.html')

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('login')
