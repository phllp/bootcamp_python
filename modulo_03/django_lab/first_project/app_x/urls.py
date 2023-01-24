from django.urls import path

from .views import index
from .views import create
from .views import update

urlpatterns = [
  path('', index, name='index'),
  path('create/', create, name='create'),
  path('update/<int:user_id>', update, name='update')
]