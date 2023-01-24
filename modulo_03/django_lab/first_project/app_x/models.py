from django.db import models

class User(models.Model):
  nome = models.CharField('nome', max_length=50)
  telefone = models.IntegerField('telefone')
  email = models.CharField('email', max_length=200)

  def __str__(self):
    return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"