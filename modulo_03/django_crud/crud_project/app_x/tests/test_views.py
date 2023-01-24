from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from app_x.models import User

class ViewTest(TestCase):
  def setUp(self):
    self.data = {
      'name': 'Name',
      'age': 'Age',
      'email': 'Email'
    }
    self.client = Client()
  
  def test_index(self):
    request = self.client.get(reverse_lazy('index'))
    self.assertEquals(request.status_code, 200)
  
  def test_create(self):
    request = self.client.get(reverse_lazy('create'), data=self.data)
    self.assertEquals(request.status_code, 200)