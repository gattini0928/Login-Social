from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255,null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome or self.user.username

