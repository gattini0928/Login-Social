from django.shortcuts import render

def homepage(request):
    return render(request, 'app/homepage.html', {'mensagem':'ola mundo'})
