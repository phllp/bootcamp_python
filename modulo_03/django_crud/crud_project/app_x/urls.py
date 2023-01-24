from django.urls import path

from .views import index, create, update, delete

urlpatterns = [
  path('', index, name='index'),
  path('create/', create, name='create'),
  path('update/<int:user_id>', update, name='update'),
  path('delete/<int:user_id>', delete, name='delete')
]