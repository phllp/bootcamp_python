from django.test import TestCase

from app_x.models import User 

class StrTest(TestCase):
  def setUp(self):
    self.user = User(name='Name', age='Age', email='Email')

  def test_str(self):
    s = '''
    Name: Name \n
    Age: Age \n
    Email: Email \n
    '''
    self.assertEquals(str(self.user), s)