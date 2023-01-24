from django.db import models

class User(models.Model):
  name = models.CharField('name', max_length=50)
  email = models.CharField('email', max_length=100)
  age = models.IntegerField('age')

  def __str__(self):
    return f'''
    Name: {self.name} \n
    Age: {self.age} \n
    Email: {self.email} \n
    '''