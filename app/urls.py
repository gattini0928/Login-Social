from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('fazerlogin/', fazer_login, name='fazer_login'),
    path('criarconta/', criar_conta, name='criar_conta'),
    path('perfil/', perfil, name='perfil'),
    path('logout/', fazer_logout, name='fazer_logout'),
    path('definir-username/', definir_username, name='definir_username'),
]
