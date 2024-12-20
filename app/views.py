from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Perfil

def homepage(request):
    return render(request, 'app/homepage.html')

def fazer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()
        if user:
            user = authenticate(
                request, username=user.username, password=senha)
            if user:
                login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f"Bem-vindo {user.username}")
                return redirect('homepage')

        messages.error(request, 'E-mail ou senha inválidos')
        return redirect('fazer_login')
    return render(request, 'app/login.html')

def criar_conta(request):
    if request.method == 'POST':
        dados = request.POST.dict()
        print(dados)
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if senha2 != senha:
            messages.error(request, 'As senhas digitadas não são iguais')
            return render(request, 'app/criar_conta.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, f'E-mail já registrado, faça login.')
            return render(request, 'app/criar_conta.html')

        username = email.split('@')[0]
        user = User.objects.create(username=username, email=email)
        user.set_password(senha)
        user.save()

        perfil = Perfil.objects.create(user=user, nome=nome)
        perfil.save()
        messages.success(request, f'Conta {user.email} criado com sucesso.')
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('definir_username')
    return render(request, 'app/criar_conta.html')


def perfil(request):
    return render(request, 'app/perfil.html')

@login_required
def definir_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            messages.error(request, 'Username é obrigatório.')
            return render(request, 'app/definir_username.html')

        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este username já está em uso.')
            return render(request, 'app/definir_username.html')
        request.user.username = username
        request.user.save()
        messages.success(request, 'Username definido com sucesso!')
        return redirect('homepage')
    return render(request, 'app/definir_username.html')

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('fazer_login')
